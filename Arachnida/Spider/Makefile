# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: MadRaven <MadRaven@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/22 11:25:01 by ffaivre           #+#    #+#              #
#    Updated: 2024/05/02 18:58:31 by ffaivre          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME			:= 	ft_ping


CC 				:= 	gcc
CFLAGS 			:= 	-Wall -Wextra -Werror


DIR_SRCS		:=	srcs
DIR_OBJS		:=	.objs
DIR_INCS		:=	incs


LST_INCS		:=	ft_ping.h \


LST_SRCS 		:=	main.c \
					parsing.c \
					init.c \
					time.c \


LST_OBJS		:=	$(LST_SRCS:.c=.o)

SRCS			:=	$(addprefix $(DIR_SRCS)/,$(LST_SRCS))
OBJS			:=	$(addprefix $(DIR_OBJS)/,$(LST_OBJS))
INCS			:=	$(addprefix $(DIR_INCS)/,$(LST_INCS))


PRINTF = LC_NUMERIC="en_US.UTF-8" printf


all:	$(NAME)


$(NAME):	$(OBJS) 
	@$(CC) $(CFLAGS) $^ -o $@
	@$(PRINTF) "\r%100s\r$(_PURPLE)$(NAME) is up to date!$(_WHITE)\n"


$(DIR_OBJS)/%.o:	$(DIR_SRCS)/%.c $(INCS) Makefile | $(DIR_OBJS)
	@$(PRINTF) "\rCompiling $(_BLUE)$<$(_WHITE)..."
	@$(CC) $(CFLAGS) -I $(DIR_INCS) -c $< -o $@


$(DIR_OBJS):
		@mkdir -p $(DIR_OBJS)



clean:
	@$(PRINTF) "$(_GREEN)Cleaning up object files in $(NAME)...$(_WHITE)\n"
	@rm -rf $(DIR_OBJS)


fclean:	clean
	@$(PRINTF) "$(_YELLOW)Removed $(NAME)$(_WHITE)\n"
	@rm -rf $(NAME)


re:	fclean all


norm:
	@$(PRINTF) "$(_CYAN)\nChecking norm for $(NAME)...$(_WHITE)\n"
	@norminette -R CheckForbiddenSourceHeader $(DIR_SRCS) $(DIR_INCS)


git:	fclean
	@$(PRINTF) "$(_RED)\nAdding GIT...$(_WHITE)\n"
	git add .
	git commit -m "Auto-Commit"
	git push



.PHONY: all clean fclean re norm git


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
