# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ffaivre <ffaivre@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/22 11:25:01 by ffaivre           #+#    #+#              #
#    Updated: 2024/06/03 12:37:59 by ffaivre          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


PRINTF = LC_NUMERIC="en_US.UTF-8" printf

all: build run

build:
	docker build -t spider-image .

run:
	docker run --rm -it spider-image

exec:
	docker exec -it spider-image bash

git:
	@$(PRINTF) "$(_RED)\nAdding GIT...$(_WHITE)\n"
	git add .
	git commit -m "Auto-Commit"
	git push


.PHONY: all build run git


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
