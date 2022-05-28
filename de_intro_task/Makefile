compose:
	sudo docker-compose --env-file ./.env.list up

rm-all:
	sudo docker rm -f $$(sudo docker ps -aq)

rmi-all:
	sudo docker rmi -f $$(sudo docker images -aq)
