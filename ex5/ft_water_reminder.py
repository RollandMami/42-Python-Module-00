# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:49:00 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:49:00 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_water_reminder():
	last_watered = int(input("Days since last watering: "))
	if last_watered > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")
