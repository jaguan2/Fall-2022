#Jason Guan
#U9893-2926
#Program intended to output the amount of ingredients needed for inputted number of cookies

cookies = float(input('Enter the number of cookies:'))
sugar = (1.5 / 48)
butter = (1 / 48)
flour = (2.75 / 48)

print(f'To make {cookies}, you will need')
print(f'{sugar*cookies:.2f} cups of sugar')
print(f'{butter*cookies:.2f} cups of butter')
print(f'{flour*cookies:.2f} cups of flour')
