# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 10:31:53 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/23 10:31:53 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    area = int(length) * int(width)
    print(f"Plot area: {area}")
