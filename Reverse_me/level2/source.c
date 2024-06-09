/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: MadRaven <MadRaven@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/09 17:52:05 by MadRaven          #+#    #+#             */
/*   Updated: 2024/06/09 19:27:26 by MadRaven         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/types.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void	ok(void)
{
	puts("Good job.");
	return ;
}


void	no(void)
{
	puts("Nope.");
	exit (1);
}


int	main(void)
{
	unsigned int uVar1;
	size_t sVar2;
	int iVar3;
	bool bVar4;
	char local_3d;
	char local_3c;
	char local_3b;
	char local_3a;
	char local_39 [24];
	char local_21 [9];
	unsigned int local_18;
	int local_14;
	int local_10;
  
	printf("Please enter key: ");
	local_10 = scanf("%23s", local_39);
	if (local_10 != 1)
		no();
	if (local_39[1] != '0' || local_39[0] != '0')
		no();
	memset(local_21, 0, 9);
	local_21[0] = 'd';
	local_18 = 2;
	local_14 = 1;
	while (true)
	{
		sVar2 = strlen(local_21);
		uVar1 = local_18;
		bVar4 = false;
		if (sVar2 < 8)
		{
			sVar2 = strlen(local_39);
			bVar4 = uVar1 < sVar2;
		}
		if (!bVar4)
			break ;
		local_3d = local_39[local_18];
		local_3c = local_39[local_18 + 1];
		local_3b = local_39[local_18 + 2];
		char tmp[4] = {local_3d, local_3c, local_3b, '\0'};
		iVar3 = atoi(tmp);
		local_21[local_14] = (char)iVar3;
		local_18 = local_18 + 3;
		local_14 = local_14 + 1;
	}
	local_21[local_14] = '\0';
	iVar3 = strcmp(local_21, "delabere");
	if (iVar3 == 0)
		ok();
	else
		no();
	return (0);
}
