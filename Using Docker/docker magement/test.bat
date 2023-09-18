docker stop $(docker ps -a -q)
docker rm -f $(docker ps -a -q)
docker rmi $(docker images -q)

build.bat
timeout 7
run.bat
