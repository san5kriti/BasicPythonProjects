# Main aim of this program: Develop Username and Password Set Up for user
# Salient points to note: Password must be at least 12 characters long 
# PLAN: Define set_username as a function where user info (name) is collected and username is set up
# PLAN: Define set_password as a function where password of user is set up 

# Introduction;
# User information is collected here for use throughout the code
user = input("What is your name? ").strip()
print("Hello " + user)

# Define a function to set up the user's username
def set_username(real_name):
    print("Set an appropriate username.")
    print("Note that your username must not be your real name for security reasons.")
    
    while True:
        username = input("What would you like to set as a username? ").strip()
        if username.lower() == real_name.lower():
            print("Your username must not be your real name!")
        else:
            print("Username: " + username)
            confirm_username = input("Confirm username? (y/n): ").strip().lower()
            if confirm_username == 'y':
                print("Great! Your username has been set: " + username)
                return username
            else:
                print("Taking you back to reset your username.")

# Set the username
username = set_username(user)

# Define a function to set up the user's password
def set_password():
    print("Password Set Up")
    print("Note that the password must be at least 12 characters long.")
    
    while True:
        password = input("Please enter a password of your choice: ").strip()
        if len(password) < 12:
            print("Password must be at least 12 characters long!")
        else:
            confirm_password = input("Re-enter your password to confirm: ").strip()
            if confirm_password == password:
                print("Great! Your password has been set.")
                return password
            else:
                print("Passwords do not match. Taking you back to setting password.")

# Set the password
password = set_password()


"""NOTES:Case Insensitivity: Usernames are compared in lowercase to prevent case mismatches using lower().
Whitespace Handling: .strip() removes extra spaces from input.
Password Check: Explicitly states passwords must be at least 12 characters long."""
