# This is just a nice Caesar’s Shifty Cipher done on upper case letters

import string


def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        substitute_letter = string.ascii_uppercase[(i + n) % alphabet_size]
        # The modulo is to cope with values higher then 26

        encoding[letter] = substitute_letter
        decoding[substitute_letter] = letter

    return encoding, decoding


def create_cipher(message, encoding):
    cipher = ""
    for char in message:
        cipher += encoding[char]
    return cipher


def plain_text(cipher, decoding):
    plain = ""
    for char in cipher:
        plain += decoding[char]
    return plain


def main():
    n = 5
    message = 'HELLO'
    encoding = {}
    decoding = {}
    encoding, decoding = create_shift_substitutions(n)
    cipher = create_cipher(message, encoding)
    print("the cipher is : {}".format(str(cipher)))
    plain = plain_text(cipher, decoding)
    print("the plain text is : {}".format(plain))


main()
