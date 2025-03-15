import string

alphabet = list(string.ascii_lowercase)

def encrypt(original_text, shift_amount):
    cipher_text = ""
    # using index function
    for char in original_text:
        if char not in alphabet:
            cipher_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    
    return cipher_text

def decrypt(original_text, shift_amount):
    decipher = ""
    for char in original_text:
        shifted_position = alphabet.index(char) - shift_amount
        shifted_position %= len(alphabet)
        decipher += alphabet[shifted_position]
    
    return decipher

def caeser(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == 'encode':
        print(encrypt(original_text=original_text, shift_amount=shift_amount))
    elif encode_or_decode == 'decode':
        print(decrypt(original_text=original_text, shift_amount=shift_amount))
    else:
        print("Incorrect inputs provided!")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    user_continue = input("Type 'yes' if you want to go agaoin, Otherwise, type 'no'. \n").lower()
    if user_continue == 'no':
        should_continue = False