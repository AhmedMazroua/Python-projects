#dynamically created password generator that requests a valid length for a password, and generates a password of that length

import random
import string

#returns a password made of chars, nums, and punctual syntax
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#defines a request for user input of a valid length, and returns a generated password utilizing a method from outside the local scope of "main"
def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))

    #conditional for length
    if length <= 0:
        print("Password length should be greater than 0.")
        return
    #calls method from outside of scope
    password = generate_password(length)
    print("Your randomly generated password is:", password)

main()
