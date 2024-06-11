# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ffaivre <ffaivre@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/22 11:25:01 by ffaivre           #+#    #+#              #
#    Updated: 2024/06/11 15:03:05 by ffaivre          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


PRINTF = LC_NUMERIC="en_US.UTF-8" printf

NAME	:= inquisitor

IMG 	:= inquisitor_img

all: build run exec

build:
	docker build -t $(NAME) .

run:
	docker run -d --name $(IMG) $(NAME)

exec:
	docker exec -u 0 -it $(IMG) bash

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


.PHONY: all build run git exec delete re rm


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
