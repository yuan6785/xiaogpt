from __future__ import annotations

from rich import print
from typing import Any

from xiaogpt.bot.base_bot import BaseBot, ChatHistoryMixin
from xiaogpt.utils import split_sentences
import requests
import json


class Ernie4Bot(ChatHistoryMixin, BaseBot):
    def __init__(self, baidu_api_key, baidu_secret_key) -> None:
        self.history = []
        #
        self.baidu_api_key = baidu_api_key
        self.baidu_secret_key = baidu_secret_key

    @classmethod
    def from_config(cls, config):
        return cls(
            baidu_api_key=config.baidu_api_key, baidu_secret_key=config.baidu_secret_key
        )

    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        access_token默认有效期30天----记得后面刷新----
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {
            "grant_type": "client_credentials",
            "client_id": self.baidu_api_key,
            "client_secret": self.baidu_secret_key,
        }
        access_token = str(
            requests.post(url, params=params, timeout=(5, 5)).json().get("access_token")
        )
        return access_token
    
    def get_ask_res(self, query):
        ak = self.get_access_token()
        url = (
            "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token="
            + ak
        )
        #
        ms = self.get_messages()
        ms.append({"role": "user", "content": f"{query}"})
        # user: 表示用户 assistant: 表示对话助手 function: 表示函数
        # api参考:  https://console.bce.baidu.com/tools/#/api?product=AI&project=%E5%8D%83%E5%B8%86%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%B9%B3%E5%8F%B0&parent=ERNIE-Bot-4&api=rpc%2F2.0%2Fai_custom%2Fv1%2Fwenxinworkshop%2Fchat%2Fcompletions_pro&method=post
        payload = json.dumps(
            {"messages": ms, "stream": False}
        )
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, headers=headers, data=payload, timeout=(10, 100))

        # print(response.text)
        res_json = response.json()
        result = res_json['result']
        print(result)
        return result


    async def ask(self, query, **options):
        r = ""
        try:
            r = self.get_ask_res(query)
        except Exception as e:
            print(str(e))
        print(r)
        return r

    def ask_stream(self, query: str, **options: Any):
        raise Exception("Bard do not support stream")
