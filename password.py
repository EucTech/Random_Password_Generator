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
    while True:
        create = input("\nCreate Password: ")
        length = len(create)

        if length < 6:
            print("\nPassword should be at least 6 charactes long.\n")
        if length == 6:
            if not any(n in create for n in string.ascii_uppercase):
                print("\nAdd at least one uppercase")
            elif not any(n in create for n in string.ascii_lowercase):
                print("\nAdd at least one lowercase")
            elif not any(n in create for n in string.digits):
                print("\nAdd at least one digits")
            elif not any(n in create for n in string.punctuation):
                print("\nAdd at least one symbol\n")
            else:
                confirm = input("\nConfirm Password: ")
                if create == confirm:
                    print("You have created your password ✅\n")
                    break
                elif not create == confirm:
                    print("\nIncorrect password")

        elif length > 6:
            print("\nPassword should not be more than 6 characters\n")


if info == 2:
    print(password)
elif not info == 1 or info == 2:
    print("Input 1 or 2")
