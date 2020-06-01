print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************\n')


print('Appetizers')
print('----------')
appetizers = ['Wings', 'Cookies', 'Spring Rolls\n']

for app in appetizers:
    print(app)

print('Entrees')
print('----------')
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden\n']

for ent in entrees:
    print(ent)

print('Desserts')
print('----------')
desserts = ['Ice Cream', 'Cake', 'Pie\n']

for des in desserts:
    print(des)

print('Drinks')
print('----------')
drinks = ['Coffee', 'Tea', 'Unicorn Tears\n']

for drk in drinks:
    print(drk)

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

orders = []
ordering = True 
while ordering == True:
    order = str(input())
    if order == 'quit':
        ordering = False
    else:
        orders.append(order)
        counting = str(orders.count(order))
        print('** ' + counting + ' order of ' + order + ' have been added to your meal **')
        
