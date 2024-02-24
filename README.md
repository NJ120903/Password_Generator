# Password_Generator

This program is a simple password manager implemented in Python using SQLite for database storage and the cryptography library for password encryption. Here's a brief overview of what the program does:

1. **Initialization:** It initializes a Fernet key for encryption/decryption and connects to an SQLite database (`passwords.db`) to store passwords.

2. **Database Setup:** If the `passwords` table doesn't exist in the database, it creates one with columns for website, username, and password.

3. **Password Generation:** It provides an option to generate a strong password for a website and username combination. The generated password is displayed to the user and then encrypted and stored in the database.

4. **Password Retrieval:** It allows the user to retrieve a password for a specific website and username combination. The password is decrypted and displayed to the user.

5. **Password Update:** It allows the user to update an existing password for a specific website and username combination. A new strong password is generated, displayed, encrypted, and then updated in the database.

6. **Menu System:** It provides a simple menu system for the user to interact with the password manager, including options to create, retrieve, and update passwords, as well as to exit the program.

This program provides a basic framework for managing passwords, but it's important to note that it's a simplified example for learning purposes and may not be suitable for production environments. It can be used as a starting point for developing more advanced password managers with additional features and security measures.
