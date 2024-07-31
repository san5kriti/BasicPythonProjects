#NOTES: This is a basic atm banking program where login system is set up using log in pin, there are functions to either check balance, withdraw or deposit.
#pin is '1234', will allow user to log in.

# Introduction function: Greets the user and prompts for their full name.
def intro():
    print("Welcome to ABC BANKING")
    user = input("Dear User, what is your Full Name?")
    global User  # Declare User as a global variable to use elsewhere.
    print("log in to your account " + user)

# Function to handle PIN entry and validation.
def pincode():
    pin = input("ENTER FOUR-DIGIT PINCODE: ")  # Prompt user for PIN.
    if pin == "1234":  # Check if PIN is correct.
        print("Login Successful")
        loginsuccess()  # Proceed to login success flow.
    else:
        print("Invalid PIN for your banking account")
        exit = input("To try again enter 'y', To exit enter 'n': ")
        if exit.lower() == 'n':  # User chose to exit.
            intro()
            pincode()
        else:  # User wants to try again.
            print("Invalid PIN")
            try2 = input("Enter Valid PIN, Please note that you have two more tries: ")
            if try2 == '1234':
                print("Login Successful")
                loginsuccess()
            else:
                print("Invalid PIN")
                try3 = input("Enter Valid PIN, Please note that this is your last try: ")
                if try3 == '1234':
                    print("Login Successful")
                    loginsuccess()
                else:
                    print("Dear user, your card has been retained and your account has been locked. Please approach BANK STAFF for assistance or CALL 1234567")
                    intro()
                    pincode()

# Function to handle actions after successful login.
def loginsuccess():
    print("Welcome")
    print('''To Check your Balance Enter 'b'
    To Withdraw Money Enter 'w'
    To Deposit Money into your account, Enter 'd'.
    To Log Out Enter 'x''')
    functions = input("What would you like to do?")

    if functions.lower() == 'b':
        checkbalance()  # Call function to check balance.
    elif functions.lower() == 'w':
        withdrawmoney()  # Call function to withdraw money.
    elif functions.lower() == 'd':
        depositmoney()  # Call function to deposit money.
    elif functions.lower() == 'x':
        print("Thank you for Banking with us! :)")
        intro()
        pincode()  # Restart the login process.
    else:
        print("Redirecting you to Login page")
        loginsuccess()  # If invalid option, restart function.

import random
balance = random.randint(100, 1000)  # Initialize random balance.
userbalance = balance  # Set user balance to initial balance.

# Function to check the current balance.
def checkbalance():
    global userbalance
    userbalance = balance  # Update user balance.
    print("You Have chosen to Check your current Balance")
    print("Total Balance = " + str(userbalance) + " pounds")
    mainpg = input("Would you like to exit? (y/n): ")
    if mainpg.lower() == 'y':
        print("Redirecting you to main page")
        loginsuccess()  # Return to main page.
    else:
        checkbalance()  # Repeat balance check if user does not exit.

# Function to withdraw money from the account.
def withdrawmoney():
    global withdrawal
    global userbalance
    global balance
    global deposit
    print("You have chosen to Withdraw Money")
    print("The total balance in your account is " + str(userbalance) + " pounds")
    withdrawal = input("How much would you like to Withdraw? Note that you can withdraw up to total of your Balance: ")
    if int(withdrawal) > int(userbalance):
        print("Insufficient Funds, Please enter valid amount to Withdraw")
        withdrawmoney()  # Retry if insufficient funds.
    else:
        balance = int(userbalance) - int(withdrawal)  # Update balance.
        print("Withdrawing " + str(withdrawal) + " from total balance of " + str(userbalance))
        userbalance = balance  # Set new user balance.
        print("Please collect cash")
        print("Remaining Balance = " + str(userbalance))
        print("Redirecting you to main page")
        loginsuccess()  # Return to main page.

# Function to deposit money into the account.
def depositmoney():
    global deposit
    global userbalance
    global balance
    print("You have chosen to Deposit Money")
    print("The total balance in your account is " + str(balance) + " pounds")
    deposit = input("What amount would you like to deposit? ")
    confirm = input("You have chosen to deposit " + str(deposit) + " pounds. Press 'y' to proceed and 'n' to cancel: ")
    if confirm == 'y':
        balance = int(userbalance) + int(deposit)  # Update balance.
        print("Depositing chosen amount into account")
        print("Updated balance = " + str(balance))
        print("Deposit successful, redirecting you to main page")
        loginsuccess()  # Return to main page.
    else:
        print("Depositing Money Cancelled, Redirecting you to main page")
        loginsuccess()  # Return to main page.

# Start the process by calling intro and pincode functions.
intro()
pincode()
