# Program Name: main.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 1
# Due Date: 01/25/2025
# Purpose: An interactive program to display
#          user input
# List Specific resources used to complete the assignment
#   * https://www.geeksforgeeks.org/how-to-catch-a-keyboardinterrupt-in-python/

def display_menu():
    """Print menu options to screen"""
    print("\nMenu Options:")
    print("1. Append data to input buffer")
    print("2. Clear input buffer")
    print("3. Display input buffer")
    print("4. Exit")


if __name__ == "__main__":
    input_buffer = ""
    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice (1-4): ")
            choice = choice.lower()

            if choice == "1":
                new_data = input("Enter text to append: ")
                input_buffer += new_data
                print("Data appended successfully.")
            elif choice == "2":
                input_buffer = ""
                print("Buffer cleared.")
            elif choice == "3":
                if input_buffer:
                    print(input_buffer)
                else:
                    print("Buffer is empty.")
            elif choice == "4":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        # Use KeyboardInterrupt to allow users to exit by
        # pressing Ctrl + C or D
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
