# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:54:27 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:54:27 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_count_harvest_recursive():
	def recursive_harvest(count, days):
		if count > days:
			return
		print("Days {}".format(count))
		return recursive_harvest(count + 1, days)
	days = int(input("Days until harvest: "))
	recursive_harvest(1, days)
	print("Harvest time!")
