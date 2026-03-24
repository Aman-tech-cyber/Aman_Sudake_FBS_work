# Write a program to calculate area of an equilateral triangle. 

import math

side = int(input('Enter the side of equilateral triangle:'))

area_of_equilateral_triangle = (1 / 4) * math.sqrt (3) * side **2

print(f'area_of_equilateral_triangle is: {area_of_equilateral_triangle}')