第一次fork后的初始化操作:
    1. fork https://github.com/yihong0618/xiaogpt 这个资源到我的github
    2. git clone git@github.com:yuan6785/xiaogpt.git   # 注意该仓库不要保存敏感信息，因为fork的仓库不能变为私有
    3. 进入我的资源目录xiaogpt
       cd xiaogpt 
       git chekcout main
       git remote add upstream https://github.com/yihong0618/xiaogpt.git
       git fetch upstream
    4. 从特定版本创建分支
       git fetch upstream
       git checkout -b fork_main upstream/v1.82
       git push --set-upstream origin fork_main
    
    5. 保证和第4步的发布tag一致, 这里tag不要和作者完全一致，无法push，版本号一致即可
       git checkout fork_main
       git tag -a yx1.82 -m "yx1.82"
       git push origin yx1.82
    


后期合并迭代操作:
    1（可选）. 合并作者的发布的版本到我本地fork的main分支，保持main分支和作者的一致(这一步仅仅是本地看，对于代码开发和合并没有任何用处)
        git checkout main
        git fetch upstream 
        git merge upstream/v1.83  
        git push

    2 (必须). 修改fork_main的内容后的发版操作
        git checkout fork_main
        git commit -am  "修改信息"
        git push
        # 下面一定注意区分是否需要同步远端
        if 1: # 如果作者远端的版本也要同步更新，则执行下面两句
            git fetch upstream 
            git merge upstream/v1.83 # 例如: git merge upstream/
            git tag -a yx1.83 -m "yx1.83"
        else: # 如果作者远端没有更新,0.1代表在1.82的基础上修改了0.1个版本------
            git tag -a yx1.82-0.1 -m "yx1.82-0.1"
        #
        git push # 将tag版本推到本地fork_main分支
        git push origin --tags # 推送所有本地tag版本到远端，也可以只推单个tag版本 git push origin yx1.82-0.1

        
调试安装(不带版本号):
    bash -c 'http_proxy=http://127.0.0.1:8118 https_proxy=http://127.0.0.1:8118  /opt/software/anconda3/envs/py310_xiaogpt/bin/pip install git+https://github.com/yuan6785/xiaogpt.git'

更新安装(需要版本号):
    bash -c 'http_proxy=http://127.0.0.1:8118 https_proxy=http://127.0.0.1:8118  /opt/software/anconda3/envs/py310_xiaogpt/bin/pip install git+https://github.com/yuan6785/xiaogpt.git@yx1.82-0.1'