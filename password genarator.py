import random
import string


def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    # Prompt user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")


if __name__ == '__main__':
    main()
