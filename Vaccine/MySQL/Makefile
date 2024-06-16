.PHONY: fclean clean prune

all:
	docker compose up --build

clean:
	docker compose down

fclean: clean
	-docker stop $(shell docker ps -qa) 2>/dev/null
	-docker rm $(shell docker ps -qa) 2>/dev/null
	-docker rmi -f $(shell docker images -qa) 2>/dev/null
	-docker volume rm $(shell docker volume ls -q) 2>/dev/null
	-docker network rm $(shell docker network ls -q) 2>/dev/null

prune	: clean
	docker system prune -f -a
