#Jason Guan
#U9893-2926
#Program intended to promot the user for item and item price inputs then formats
#into a receipt

class Retail_Item:
    def __init__(self, name, amount, price):
        self.__name = name
        self.__amount = amount
        self.__price = price

    def __str__(self):
        output = '{:<20}{:<10}${:<10.2f}'.format(self.__name, self.__amount, self.__price)
        return output

def main():
    name = input('Name of item 1: ')
    amount = int(input(
        'Amount of item 1: '))
    price = float(input(
        'Price of item 1: '))
    item1 = Retail_Item(name, amount, price)

    print()
    
    name = input('Name of item 2: ')
    amount = int(input(
        'Amount of item 2: '))
    price = float(input(
        'Price of item 2: '))
    item2 = Retail_Item(name, amount, price)

    print()
    print('Here is a summary of the items you added:')
    print('{:<20}{:<10}{:<10}'.format('Item', 'Amount', 'Price'))
    print('---------------------------------------------------')
    print(item1)
    print(item2)

main()
