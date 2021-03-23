/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   caesar_decrypt.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amalsago <amalsago@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/03/23 11:18:40 by amalsago          #+#    #+#             */
/*   Updated: 2021/03/23 15:52:34 by amalsago         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

/*
** E(x) = (x + n) % 26
** D(x) = (x - n) % 26
*/

int		main(int ac, char **av)
{
	int	i;
	int	j;

	i = -1;
	if (ac != 2)
		return (1);
	while (i++ < 25)
	{
		j = -1;
		printf("+%-2d ", i);
		while (av[1][++j])
			printf("%c", ((av[1][j] - 'a' + i) % 26) + 'a');
		printf("\n");
	}
	return (0);
}
