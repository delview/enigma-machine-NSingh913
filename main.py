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
            



# Ask the user to input the message 

# Ask the user do they want to encrypt or decrypt a message

# Ceate a function to encrypt a message

# Create a function to decrypt a message

 