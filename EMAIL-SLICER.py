
# Python Email Slicer : A simple program to slice and extract parts of an email address.

email = input("Enter your email address: ")

# Slicing the email to get the username and domain from the @ character :

index = email.index('@')

Username = email[:index]
Domain = email[index:]

print(f'Your username is: {Username} and your domain is: {Domain}')

# Example :
# Input: python-pro@gmail.py.in
# Output: Your username is: python-pro and your domain is: @gmail.py.in


