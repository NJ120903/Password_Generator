import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_chars = lower_case + upper_case + digits + special_chars

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate and display password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid length (a positive integer).")

if __name__ == "__main__":
    main()
