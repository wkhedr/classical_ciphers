def vigenere_cipher(message, key, decrypt=False):
    """
    Encrypt or decrypt a message using the Vigenère cipher.

    Args:
    message (str): The message to encrypt or decrypt.
    key (str): The encryption or decryption key.
    decrypt (bool): If True, decrypt the message. Otherwise, encrypt it. Default is False.

    Returns:
    str: The encrypted or decrypted message.
    """

    # Make sure the key is long enough to encrypt the message
    key = key * (len(message) // len(key) + 1)

    # Convert the message and key to uppercase
    message = message.upper()
    key = key.upper()

    result = ""
    for i in range(len(message)):
        if message[i].isalpha():
            if decrypt:
                # Decrypt the current letter
                letter = chr((ord(message[i]) - ord(key[i])) % 26 + ord('A'))
            else:
                # Encrypt the current letter
                letter = chr((ord(message[i]) + ord(key[i])) % 26 + ord('A'))
            result += letter
        else:
            # If the current character is not a letter, leave it unchanged
            result += message[i]

    return result


def main():
    # Encrypt the message "HELLO" with the key "WORLD"
    encrypted = vigenere_cipher("HELLO CRYPTOGRAPHY", "WORLD")
    print(encrypted)  # prints "DSCWR"

    # Decrypt the encrypted message with the same key
    decrypted = vigenere_cipher(encrypted, "WORLD", decrypt=True)
    print(decrypted)  # prints "HELLO"


if __name__ == "__main__":
    main()
