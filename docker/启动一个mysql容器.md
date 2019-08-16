1. 抓取镜像  
    - 抓取docker镜像仓库中最新版本的镜像
    `docker pull mysql`
    - 抓取指定版本的镜像
    `docker pull mysql:5.7`

1. 启动mysql容器
    `docker run --name 'webbook_mysql' -v /Users/Shawn:/Shawn -p 53306:3306 -e MYSQL_ROOT_PASSWORD=sxn@123 -d mysql`
    - 参数解释
        - --name 指定启动容器的名字
        - -v 映射宿主机目录到容器中，冒号前半部分为宿主机目录(/Users/Shawn)，后半部分为容器目录(/Shawn)
        - -p 映射容器端口号到宿主机端口号，冒号前半部分为宿主机端口号(53306)，后半部分为容易端口号(3306)
        - -e 设置部分环境变量，当前容器该环境变量表示数据库root账号密码
        - -d 容器后台运行
        - mysql docker镜像名称，使用`docker image ls`命令可以查询当前宿主机上有什么类型的镜像
    如果宿主环境中有多个版本的mysql镜像，可以指定tag启动容器
    `docker run ... -d mysql:5.7`
    - 映射配置文件，数据目录
    `docker run --name 'webbook_mysql' -v /Users/Shawn/gitee/BookWeb/database/mysql/my.cnf:/etc/mysql/my.cnf -v /Users/Shawn/gitee:/gitee -p 53306:3306 -e MYSQL_ROOT_PASSWORD=sxn@123 -d mysql:5.7`
1. 查看容器运行状态  
    `docker container ls`

1. 交互式进入容器  
    `docker exec -it containerid/name bash`

1. 交互式进入容器，支持中文
    `docker exec -ti containerid/name env LANG=C.UTF-8 bash`

