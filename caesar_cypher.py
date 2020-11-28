#####################################################################
# Final Project - Caesar Cipher
#####################################################################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_text = ""
    idx_loop = 0
    for char in text:
        idx_alphabet = alphabet.index(char.lower())
        idx_total = idx_alphabet + shift
        if idx_total > 25:
            idx_total %= 26
        encrypted_text += alphabet[idx_total]
        idx_loop += 1
    print(f"The encoded text is {encrypted_text}")


encrypt(text=text, shift=shift)
