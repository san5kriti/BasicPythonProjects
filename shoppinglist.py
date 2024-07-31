# Shopping List 
'''this is a shopping list program with three functions, view list, add items and remove them.'''

# Function to welcome the user
def welcome_user():
    print("Welcome to your Shopping List App! :D")
    user = input("What is your name? ")
    print(f"Hello {user}! This is your very own shopping list application.")

# Function to display available options
def display_options():
    print('''\nAvailable Options:
1. Check Current List
2. Add to Existing Shopping List
3. Amend Shopping List
''')

# Function to handle user options
def handle_options():
    current_list = ["eggs", "milk", "bread"]  # Initial shopping list

    while True:
        display_options()
        try:
            option = int(input("What would you like to do? Enter the number of your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if option == 1:
            print("Here is your current Shopping List:")
            print(current_list)
        elif option == 2:
            add_item = input("What item would you like to add? ")
            current_list.append(add_item)
            print("Here is your updated shopping list:")
            print(current_list)
        elif option == 3:
            print("You have chosen to make amends to your list.")
            remove_item = input("Would you like to remove an item? (y/n): ").strip().lower()
            if remove_item == 'y':
                item_to_remove = input("What item would you like to remove? ")
                if item_to_remove in current_list:
                    current_list.remove(item_to_remove)
                    print(f"{item_to_remove} has been removed from your list.")
                else:
                    print(f"{item_to_remove} is not in the shopping list.")
                print("Here is your updated shopping list:")
                print(current_list)
            elif remove_item == 'n':
                print("No items will be removed.")
            else:
                print("Invalid response. No changes made.")
        else:
            print("Invalid option. Please choose a number between 1 and 3.")
            continue

        # Ask if the user wants to go back to options
        go_back = input("Would you like to go back to options? (y/n): ").strip().lower()
        if go_back != 'y':
            print("Thank you for using the Shopping List App! Goodbye!")
            break

# Run the application
if __name__ == "__main__":
    welcome_user()
    handle_options()
