version=`date "+%H-%M-%S_%d-%m-%y"`
echo $version

docker build -t qa-ui .
docker tag qa-ui qa-ui-version

#docker run -p 80:8080 -e qa_ip='host.docker.internal' -e qa_port=85 qa-ui