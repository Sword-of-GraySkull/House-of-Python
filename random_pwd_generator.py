# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:38:26 2020

@author: Venni
"""

# Importing Modules
from string import ascii_letters, digits, punctuation
import random

# Creating a bag of characters
symbols = ascii_letters, digits, punctuation

# Getting Secure Randomisation
secure_random = random.SystemRandom()

# Generating a 10 Character Password
password = "".join(secure_random.choice(symbols) for i in range(10))

# Printing the random 10 character password
print(password)

#~~~ to create a ten-character alphanumeric password with at least one lowercase
#        character, at least one uppercase character, and at least three digits,"
# =============================================================================
# import string
# alphabet = string.ascii_letters + string.digits
# while True:
# password = ''.join(choice(alphabet) for i in range(10))
# if (any(c.islower() for c in password)
# and any(c.isupper() for c in password)
# and sum(c.isdigit() for c in password) >= 3):
# break
# =============================================================================
