discount = 0.1
subTotal = 0.0
salePrice = 0.0
layout = ''
def discountPrice (total):
    newTotal = 0.0
    saving = 0.0

    if (total >= 50):
        saving = total * discount
        newTotal = total - saving
    else:
        newTotal = total
    return (newTotal)

subTotal = float (input ('Enter the subtotal of your shopping '))
salePrice = discountPrice (subTotal)
layout = 'Sale price is £{:.2f}'
print (layout.format(salePrice))
