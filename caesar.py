# function to do Brute Force attack on a given ciphertext

def brute_force(ciphertext):
    for key in range(1, 26):
        print("Key: ", key, " Plaintext: ", decrypt(ciphertext, key))


def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            plaintext += char
    return plaintext


def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext


def main():
    plaintext = "HELLO, WORLD!"
    key = 3
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext: ", ciphertext)
    brute_force(ciphertext)


if __name__ == "__main__":
    main()
