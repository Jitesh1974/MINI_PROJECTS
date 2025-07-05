import random

options = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()+-*/<>?`~'
n = 8 #number of characters 
password = ''

for _ in range(n):
    password += random.choice(options)

print("Generated password:", password)
