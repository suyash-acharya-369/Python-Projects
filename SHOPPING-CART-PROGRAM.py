#Shopping Cart Program :

foods = []
prices = []
total = 0

while True :
    food = input('Enter the food name (q,Q to quit) :')
    if food.lower() == 'q':
        break
    else:
        price = int(input(f'Enter the price of {food} :'))
        foods.append(food)
        prices.append(price)

print('_____YOUR CART ______')        

for x in foods :
    print(x,end=' ')
print()
for price in prices :
    total+=price
print(f'Your total cart value is ₹{total}')
    

