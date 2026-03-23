# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:34:28 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:34:28 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_harvest_total():
	d1 = int(input("Day 1 harvest: "))
	d2 = int(input("Day 2 harvest: "))
	d3 = int(input("Day 3 harvest: "))
	total_harvest = d1 + d2 + d3
	print(f"Total harvest: {total_harvest}")
