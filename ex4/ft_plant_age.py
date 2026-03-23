# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:44:07 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:44:07 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
