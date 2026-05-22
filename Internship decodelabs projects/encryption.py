#Project 2: Basic Encryption & Decryption
# Basic Encryption & Decryption Project
# Caesar Cipher Method

print("=== Basic Encryption & Decryption ===")

# get message from user
message = input("Enter your message: ")

# shift value
shift = 5

encrypted_text = ""

# ENCRYPTION
for char in message:
    
    # check uppercase letters
    if char.isupper():
        encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

    # check lowercase letters
    elif char.islower():
        encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

    # keep spaces and symbols unchanged
    else:
        encrypted_text += char

print("\nEncrypted Text:", encrypted_text)

# DECRYPTION
decrypted_text = ""

for char in encrypted_text:

    # check uppercase letters
    if char.isupper():
        decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

    # check lowercase letters
    elif char.islower():
        decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

    # keep spaces and symbols unchanged
    else:
        decrypted_text += char

print("Decrypted Text:", decrypted_text)