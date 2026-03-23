# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 11:15:30 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 11:15:30 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if (unit == "packets"):
		print(f"{seed_type.capitalize()} seeds: {quantity} available")
	elif (unit == "grams"):
		print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
	elif (unit == "area"):
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")