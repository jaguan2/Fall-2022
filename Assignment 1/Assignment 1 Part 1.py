#Jason Guan
#U9893-2926
#Program intended to calculate the minimum runway length needed for an airplane
#when given acceleration, and take-off speed

v = input("Enter the plane's take off speed in m/s: ")
v = float(v)
a = input("Enter the plane's acceleration in m/s: ")
a = float(a)

minLength = ((v ** 2)/(2*a))
print(f'The minimum runway length needed for this airplane is {minLength:.4f} meters')
