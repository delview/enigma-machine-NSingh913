# This is a enigma machine and this will code your words into secret codes and you can also decode it

# Greet the user
print("Welcome to the Enigma Machine! ")

# Create a function to encrypt or decrypt any message using a Caeser cipher.
def ceaser_cipher(text, shift, encrypt=True):

    """
    Encrypts or decrypts a message using a simple shift cipher.
    """

    result = ""  # This stroes the final encrypted or decrypted message.
    if not encrypt:
        shift = - shift 

    # Loop through each character in the text.
    for char in text:
        if char.isalpha(): # this shift letters.
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base )
        else:
            new_char = char
        result += new_char

    return result

# Function to ask the user do they want to encrypt or decrypt a message.
def get_user_choice():

    """
    Ask the user if they want to encrypt or decrypt any message.
    """

    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Q to Quit): ").strip().lower()
        if choice in ['e', 'd', 'q']:
            return choice
        print("Invalid choice. Enter E, D, or Q. ")

# Ceate a function to get a valid shift value from the user
def get_shift_value():
    
    """
    Gets a valid shift values (1-25) from the user.
    """

    while True:
        try: 
            shift = int(input("Enter shifts value (1-25): ").strip())
            if 1 <= shift <=  25:
                return shift
            else:
                print("Shift values must be between 1 and 25. ")
        except ValueError:
            print("Please enter a valid integer. ")

# Create a main function to run the program.
def main():

    """
    Runs the enigma machine program.
    """

    while True:
        # Ask the user for their choice
        choice = get_user_choice()
        if choice == 'q':
            print(" Thank you for using Ceaser Cipher! ")
            break

        # Get the messgae from the user 
        message = input("Enter your message: ").strip()

        # Get the shift value
        shift = get_shift_value()

        # Determine whether to encrypt or decrypt
        encrypt = choice == 'e'

        # Encrypt or decrypt the message
        result = ceaser_cipher(message, shift, encrypt)

        # Display the results
        print("Result:", result)

# Run the program
if __name__ == "__main__":
    main()
 
