1. docker run -i --name test alpine：执行后进入容器，无命令提示符，可执行命令；exit退出后，容器删除。 
2. docker run -t --name test alpine：执行后进入容器，有命令提示符，执行命令无结果返回；无法退出容器。 
3. docker run -d --name test alpine：执行后退出容器，容器删除。 
4. docker run -it --name test alpine：执行后进入容器，有命令提示符，可执行命令；exit退出后，容器删除。 
5. docker run -id --name test alpine：执行后退出容器；docker exec -it test /bin/sh可再次进入容器，有命令提示符，可执行命令，exit退出后，容器未删除；docker attach test可再次进入容器，无命令提示符，可执行命令，exit退出后，容器删除，ctrl+p&q，无法退出；
6. docker run -td --name test alpine：执行后退出容器；docker exec -it test /bin/sh可再次进入容器，有命令提示符，可执行命令，exit退出后，容器未删除；docker attach test可再次进入容器，有命令提示符，执行命令无结果返回；exit、ctrl+p&q无法退出容器，需要使用ctrl+c；需要手动删除容器。 
7. docker run -itd --name test alpine：执行后退出容器；docker exec -it test /bin/sh可再次进入容器，有命令提示符，可执行命令，exit退出后，容器未删除；docker attach test可再次进入容器，有命令提示符，可执行命令；exit、ctrl+p&q退出容器；需要手动删除容器。