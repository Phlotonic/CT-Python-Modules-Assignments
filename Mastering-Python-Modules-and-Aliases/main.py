# Import the custom module text_utils using an alias tu
import text_utils as tu

# Take user input for the string
input_string = input("Enter a string: ")

# Ask the user what operation they want to perform
choice = input("Do you want to (1) Reverse the string, (2) Capitalize the string, (3) Both, or (4) Exit? Enter 1, 2, 3, or 4: ")

# Perform the chosen operation
if choice == '1':
    # Reverse the string
    reversed_string = tu.reverse_string(input_string)
    print(f"Reversed String: {reversed_string}")
elif choice == '2':
    # Capitalize the string
    capitalized_string = tu.capitalize_string(input_string)
    print(f"Capitalized String: {capitalized_string}")
elif choice == '3':
    # Reverse and capitalize the string
    reversed_string = tu.reverse_string(input_string)
    capitalized_string = tu.capitalize_string(input_string)
    print(f"Reversed String: {reversed_string}")
    print(f"Capitalized String: {capitalized_string}")
elif choice == '4':
    # Exit the program
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
