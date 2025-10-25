# ENCRYPTION PROGRAM IN PYTHON :

import random
import string

# To get all the special characters and digits and alphabets for encryption :

chars = string.punctuation + string.ascii_letters + string.digits + " "
#print(chars)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 


# Now we will store them in a list
chars = list(chars)
# print(f'chars : {chars}')

# Now we will create a key to shuffle it further :
key = chars.copy()
random.shuffle(key)
# print(f'Shuffled key : {key}')

# Now let's Encrypt :

plain_text = input('Enter a message to encrypt: ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f'Your Encrypted message : {cipher_text}')

# Now let's decrypt our message :

cipher_text = input('Enter a message to Decrypt: ')
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f'Your Decrypted message : {plain_text}')



# This is the basic version but not secure