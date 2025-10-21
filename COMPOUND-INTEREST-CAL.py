# Python Compound Interest Calculator :

# Amount = P(1+(r/n))^nt

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print('Principle cannot be negative or equal to zero. Try Again.')

while rate <=0:
    rate = float(input("Enter the interest rate : "))
    if rate <= 0:
        print('rate cannot be negative or equal to zero. Try Again.')

while time <=0:
    time = int(input("Enter the time in years : "))
    if rate <= 0:
        print('time cannot be negative or equal to zero. Try Again.')    

Amount = principle * (1 + (rate/100))**time     

print(f'The total amount after {time} years is : {Amount}')

# Example :
# Input: principle = 1000, rate = 5, time = 10
# Output: The total amount after 10 years is : 1628.894626777    


