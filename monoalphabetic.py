import string
import random


def generate_key():
    """Generate a random permutation of the 26 alphabetic characters."""
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    key = dict(zip(string.ascii_lowercase, alphabet))
    print(key)
    return key


def encrypt(message, key):
    """Encrypt the given message using Monoalphabetic Cipher with the given key."""
    ciphertext = ""
    for char in message:
        if char.isalpha():
            ciphertext += key[char]

        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    """Decrypt the given ciphertext using Monoalphabetic Cipher with the given key."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            for k, v in key.items():
                if v == char:
                    plaintext += k

        else:
            plaintext += char
    return plaintext


def main():
    message = "hello world"
    key = generate_key()

    ciphertext = encrypt(message, key)
    print(ciphertext)  # prints a different ciphertext each time

    plaintext = decrypt(ciphertext, key)
    print(plaintext)  # prints "hello world"


if __name__ == "__main__":
    main()
