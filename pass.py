import string
import secrets
import sqlite3
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Initialize the key
key = generate_key()
cipher_suite = Fernet(key)

# Connect to the SQLite database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create a table to store passwords
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (website TEXT, username TEXT, password TEXT)''')
conn.commit()

# Function to encrypt password
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())

# Function to decrypt password
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()

# Function to generate a strong password
def generate_strong_password(length=12):
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(charset) for _ in range(length))

# Function to store a password
def store_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = generate_strong_password()
    print(f"Generated password: {password}")
    encrypted_password = encrypt_password(password)
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, encrypted_password))
    conn.commit()
    print("Password saved.")

# Function to retrieve a password
def retrieve_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    c.execute("SELECT password FROM passwords WHERE website=? AND username=?", (website, username))
    encrypted_password = c.fetchone()
    if encrypted_password:
        print("Password:", decrypt_password(encrypted_password[0]))
    else:
        print("Password not found.")

# Function to update a password
def update_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = generate_strong_password()
    print(f"Generated new password: {password}")
    encrypted_password = encrypt_password(password)
    c.execute("UPDATE passwords SET password=? WHERE website=? AND username=?", (encrypted_password, website, username))
    conn.commit()
    print("Password updated.")

# Menu function
def menu():
    while True:
        print("\n1. Create a password")
        print("2. Retrieve a password")
        print("3. Update a password")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            store_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            update_password()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
menu()

# Close the database connection
conn.close()