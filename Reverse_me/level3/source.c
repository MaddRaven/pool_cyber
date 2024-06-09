/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: MadRaven <MadRaven@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/09 19:00:03 by MadRaven          #+#    #+#             */
/*   Updated: 2024/06/09 20:17:35 by MadRaven         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/types.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void	____syscall_malloc(void)
{
	puts("Good job.");
	return ;
}


void	___syscall_malloc(void)
{
	puts("Nope.");
	exit(1);
}

int	main(void)
{
	unsigned long	uVar1;
	int				iVar2;
	size_t			sVar3;
	bool			bVar4;
	char			local_4c;
	char			local_4b;
	char			local_4a;
	char			local_49;
	char			local_48[31];
	char			local_29[9];
	unsigned long	local_20;
	int				local_18;
	int				local_14;
	int				local_10;
  
	printf("Please enter key: ");
	local_10 = scanf("%39s", local_48);
	if (local_10 != 1)
		___syscall_malloc();
	if (local_48[1] != '2' || local_48[0] != '4')
		___syscall_malloc();
	memset(local_29, 0, 9);
	local_29[0] = '*';
	local_49 = 0;
	local_20 = 2;
	local_14 = 1;
	while (true)
	{
		sVar3 = strlen(local_29);
		uVar1 = local_20;
		bVar4 = false;
		if (sVar3 < 8)
		{
			sVar3 = strlen(local_48);
			bVar4 = uVar1 < sVar3;
		}
		if (!bVar4)
			break ;
		local_4c = local_48[local_20];
		local_4b = local_48[local_20 + 1];
		local_4a = local_48[local_20 + 2];
		char temp[4] = {local_4c, local_4b, local_4a, '\0'};
        iVar2 = atoi(temp);
		local_29[local_14] = (char)iVar2;
		local_20 = local_20 + 3;
		local_14 = local_14 + 1;
	}
	local_29[local_14] = '\0';
	local_18 = strcmp(local_29, "********");
	if (local_18 == -2)
		___syscall_malloc();
	else if (local_18 == -1)
		___syscall_malloc();
	else if (local_18 == 0)
		____syscall_malloc();
	else if (local_18 == 1)
		___syscall_malloc();
	else if (local_18 == 2)
		___syscall_malloc();
	else if (local_18 == 3)
		___syscall_malloc();
	else if (local_18 == 4)
		___syscall_malloc();
	else if (local_18 == 5)
		___syscall_malloc();
	else if (local_18 == 0x73)
		___syscall_malloc();
	else
		___syscall_malloc();
	return (0);
}
