/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: MadRaven <MadRaven@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/09 13:24:06 by MadRaven          #+#    #+#             */
/*   Updated: 2024/06/09 13:59:16 by MadRaven         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdio.h>

int	main(void)
{
	char	entry[1000];

	printf("Please enter key: ");
	scanf("%s", entry);
	if (strcmp(entry, "__stack_check") != 0)
		printf("Nope.\n");
	else
		printf("Good job.\n");
	return (0);
}
