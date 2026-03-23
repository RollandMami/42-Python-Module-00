# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:53:38 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:53:38 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print(f"Day {i}")