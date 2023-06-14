#!/usr/bin/python3

import random
import string

print("\nGET YOUR PASSWORD\n")
create = "1 Create your password manualy\n"
generate = "2 Generate your password randomlly\n"
print(create)
print(generate)
info = 0

user_info = input("Enter 1 to create manually and 2 to generate randomly: ")

if user_info.isalpha() or user_info in string.punctuation:
    print("Invalid input, Enter 1 or 2")
    exit()
else:
    info = int(user_info)

password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=15))

if info == 1:
    create = input("\nCreate Password: ")
    while create <= 15:
        if not any(char.isupper() for char in created):
            print("Add upper")


if info == 2:
    print(password)
else:
    print("Input 1 or 2")
