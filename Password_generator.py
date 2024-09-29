import random
import string

list=string.ascii_letters+string.digits+string.punctuation
length=int(input("Enter password length : "))
print(''.join([random.choice(list) for _ in range(length)]))