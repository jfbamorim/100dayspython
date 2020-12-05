from dayeight import caesar_cypher_art

#####################################################################
# Final Project - Caesar Cipher
#####################################################################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_cypher_art.logo)


def caesar(text, shift, direction):
    text_output = ""
    for char in text:
        if char.isalpha():
            idx_alphabet = alphabet.index(char.lower())
            if direction.lower() == 'encode':
                idx_total = idx_alphabet + shift
                if idx_total > 25:
                    idx_total %= 26
                text_output += alphabet[idx_total]
            elif direction.lower() == 'decode':
                idx_total = idx_alphabet - shift
                text_output += alphabet[idx_total]
        else:
            text_output += char
    print(f"The {direction}d text is {text_output}")


answer = "yes"
while answer == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    answer = input("Type yes if you want to go again. Otherwise type no.").lower()
print("Good bye.")


# 1st implementation
#def encrypt(text, shift):
#    encrypted_text = ""
#    for char in text:
#        idx_alphabet = alphabet.index(char.lower())
#        idx_total = idx_alphabet + shift
#        if idx_total > 25:
#            idx_total %= 26
#        encrypted_text += alphabet[idx_total]
#    print(f"The encoded text is {encrypted_text}")


#def decrypt(text, shift):
#    decrypted_text = ""
#    for char in text:
#        idx_alphabet = alphabet.index(char.lower())
#        idx_total = idx_alphabet - shift
#        decrypted_text += alphabet[idx_total]
#    print(f"The decoded text is {decrypted_text}")


#if direction.lower() == 'encode':
#    encrypt(text=text, shift=shift)
#elif direction.lower() == 'decode':
#    decrypt(text=text, shift=shift)