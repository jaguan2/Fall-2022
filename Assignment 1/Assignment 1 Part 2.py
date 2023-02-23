#Jason Guan
#U9893-2926
#Program intended to find the area of an shaded region when given the lengths of p, q and r

import math

p = float(input('Enter the first diagonal length:'))
q = float(input('Enter the second diagonal length:'))
r = float(input('Enter the radius of the enclosed circle:'))

shadeArea= ((p*q)/2) - (math.pi* (r**2))
print(f'The shaded area is {shadeArea:.3f} square units.')


