#CTI 110
#P3HW2 - Software Sales
#Maribelle sutcliffe
#February 23, 2018

numberOfPackages = int(input('Enter number of packages purchased: '))
package = 99
if numberOfPackages < 10:
    discount = 0
elif numberOfPackages < 20:
    discount = 0.10
elif numberOfPackages < 50:
    discount = 0.20
elif numberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40


total = numberOfPackages * package
discountAmount = discount * total
totalAmount = total - discountAmount

print('Amount of discount: $' + format(discountAmount, ',.2f'))
print('Total amount:  $' + format(totalAmount, ',.2f'))
