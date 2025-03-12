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

    While True:
        choice = input("Do you want to (E)ncrypr or (D)ecrypt a message? (Q to Quit): ").strip().lower()
        if choice in ['e', 'd', 'q']:
            return choice
        print("Invalid choice. Enter E, D, or Q. ")

# Ceate a function to encrypt a message

# Create a function to decrypt a message

 