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
    


后期合并迭代操作:
    1（可选）. 合并作者的发布的版本到我本地fork的main分支，保持main分支和作者的一致(这一步仅仅是本地看，对于代码开发和合并没有任何用处)
        git checkout main
        git fetch upstream 
        git merge upstream/tag-release-name  # 例如: git merge upstream/v1.82
        git push

    2 (必须). 合并第一步的版本内容到我修改过的分支fork_main， 这一步才是真正的合并作者的代码到我修改的分支
        git checkout fork_main
        git fetch upstream 
        git merge upstream/tag-release-name # 例如: git merge upstream/v1.83
        git push

