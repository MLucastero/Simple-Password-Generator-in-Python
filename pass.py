
import random
up = 'ABCDEFGHIJKLMNOPQRSTUVWXWZ'
low = 'abcdefghijklmnopqrstuvwxyz'
number = '123456789'
symbol = " !@#$%^&*()><[]"

all = up + low + number + symbol
length = 9
password = "".join(random.sample(all, length))
print('')
print('')
print("----------------------------")
print("Your password is: ", password)
print("----------------------------")
print('')
print('')
print('')