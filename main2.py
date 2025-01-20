# Function to check if a character is an alphabet
def is_alphabet(char):
    if char.isalpha():
        return True
    else:
        return False

# Get user input
user_input = input("Enter a character: ")

# Check if the input is a single character
if len(user_input) == 1:
    if is_alphabet(user_input):
        print(f"'{user_input}' is an alphabet.")
    else:
        print(f"'{user_input}' is not an alphabet.")
else:
    print("Please enter a single character.")