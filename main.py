from datetime import datetime
name = input('Enter your name:')
# printing list of items

lists = '''
rice     ----> Rs 20/kg
sugar    ----> Rs 10/kg
tea      ----> Rs 80/kg
maggi    ----> Rs 120/kg
dal      ----> Rs 90/kg
boost    ----> Rs 100/kg
colgate  ----> Rs 60/1pac
'''
# Decleration

price = 0
price_list = []
total_price = 0
final_price = 0
ilist = []
qlist = []
plist = []

# rates for items
items = {'rice': 20, 'sugar': 10, 'tea': 80, 'maggi': 120,
         'dal': 90, 'boost': 100, 'colgate': 60}
option = int(input('For list of items enter 1'))
if option == 1:
    print(lists)
else:
    print('your chance is completed ou want list go and come again')
for i in range(len(items)):
    inp1 = int(input('If you want to buy items enter 1 otherwise enter 2 for exit:'))
    if inp1 == 2:
        break

    if inp1 == 1:
        item = input('Enter your items:')
        Quantity = int(input('Enter your quantity:'))
        if item in items.keys():
            price = Quantity*(items[item])
            price_list.append((item, Quantity, items, price))
            total_price += price
            ilist.append(item)
            qlist.append(Quantity)
            plist.append(price)
            gst = (total_price*5)/100
            final_amount = gst+total_price
        else:
            print(' Sorry u entered item is not available i my store')
    else:
        print('* --> shopping is not yet completed due to u enter wrong input number , if u want exit enter 2:')
        print('you entered input is :', inp1)
# Billing

inp = int(input('can i bill the items 1 otherwise enter any number'))
if inp == 1:
    print(50 * '=')
    print(6*'>', 'please wait... bill printing', 6*'<')
    print(50*'=')
    if final_amount != 0:
        print(25 * '=', "Harsha's Super Market", 25 * '=')
        print(28 * " ", "Simhadripuram")
        print('Name :', name)
        print("Date & Time:", datetime.now())
        print(75 * '-')
        print("S.No", 5 * " ", ' items', 3 * ' ', 'Quantity', 3 * ' ', 'price')
        for i in range(len(price_list)):
            print(i, 9 * ' ', ilist[i], 6 * ' ', qlist[i], 10 * ' ', plist[i])
        print(75 * '-')
        print(40 * ' ', 'TotalAmount:', 'Rs', final_amount)
        print(75 * ' ')
        print(25 * ' ', 'ThanKs For Visiting')
        print(75 * '-')
    else:
        print('Thanks for visiting next time buy any one at least ')


else:
    print('billing stopped by u')



