#Jason Guan
#U9893-2926
#Program that calculates tip number and total when given the subtotal and gratuity rate

subTotal = float(input('Enter the Subtotal: $'))
gratuityRate = float(input('Enter the amount(as a %):'))
tip = gratuityRate/100 * subTotal
total = subTotal + tip

print(f'Subtotal: $ {subTotal:,.2f}')
print(f'Tip: $ {tip:,.2f}')
print(f'Total: ${total:,.2f}')
