# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ffaivre <ffaivre@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/22 11:25:01 by ffaivre           #+#    #+#              #
#    Updated: 2024/06/12 15:32:35 by ffaivre          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


PRINTF = LC_NUMERIC="en_US.UTF-8" printf

NAME	:= inquisitor

IMG 	:= inquisitor_img

all: down build

build:
	docker compose up --build

down:
	docker compose down

inquisitor: show
	docker exec -it inquisitor bash

server:
	docker exec -it server sh

client:
	docker exec -it client sh

delete:
	docker stop $(shell docker ps -aq) || true
	docker rm $(shell docker ps -aq) || true
	docker rmi $(shell docker images -aq) || true
	docker system prune -af

rm:
	docker stop $(shell docker ps -aq) || true
	docker rm $(shell docker ps -aq) || true
	docker rmi $(shell docker images -aq) || true

re: rm all

git:
	@$(PRINTF) "$(_RED)\nAdding GIT...$(_WHITE)\n"
	git add .
	git commit -m "Auto-Commit"
	git push


SERVER	:= server
CLIENT	:= client

IP_SV := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER))
MAC_SV := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER))
IP_CL := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT))
MAC_CL := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(CLIENT))

show:
	@echo "Use: "
	@echo ./inquisitor $(IP_SV) $(MAC_SV) $(IP_CL) $(MAC_CL)

.PHONY: all build run git exec delete re rm down inquisitor server client


# Colors
_GREY		= \033[38m
_RED		= \033[91m
_GREEN		= \033[92m
_YELLOW		= \033[33m
_BLUE		= \033[34m
_PURPLE		= \033[35m
_CYAN		= \033[36m
_WHITE		= \033[37m
_MAGENTA 	= \033[95m
