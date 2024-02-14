import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))

    if length <= 0:
        print("Password length should be greater than 0.")
        return

    password = generate_password(length)
    print("Your randomly generated password is:", password)

if __name__ == "__main__":
    main()
