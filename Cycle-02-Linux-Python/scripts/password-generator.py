import random
import string

length = int(input("Enter password length: "))
count = int(input("How many passwords: "))

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Password {i+1}: {password}")
