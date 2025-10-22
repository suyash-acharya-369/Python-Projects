# CONCESSION STAND PROGRAM USING PYTHON DICTIONARY :

menu = {'samosa': 15,
        'kachori' : 10,
        'jalebi' : 20,
        'poha' : 10,
        'aloo-vada' : 15,
        'vada-pav' : 25,
        'daveli' : 30,
        'gulab-jamun' : 5,
        'aloo-patty' : 7}

cart = []
total = 0

for key, value in menu.items():
    print(f'{key:15} : ₹{value:.2f}')

print('______________________________________________')    

while True :
    food = input('Select the food (q to quit) :').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None :
        cart.append(food)   

print('_____________________YOUR ORDER_________________')
for food in cart :
    total += menu.get(food)
    print(food,end=' ')

print()
print(f'Your total cart value is {total:.2f}')    

