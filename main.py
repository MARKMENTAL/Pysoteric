shift = 3

text = input("Welcome to the first release of Pysoteric! Enter a string of text to be encrypted \n")

encryption = ""

invalid = 0

ciphermethod = input("Now enter a cipher method to be used. 3 for caesar based(weakest), 4 for 4 shift(stronger) or 6 "
                     "for the sixer cipher(strongest) \n")

for c in text:
    if c and ciphermethod == '3':
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        new_index = (c_index + shift) % 52

        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)

        encryption = encryption + new_character

    elif c and ciphermethod == '4':
        shift = 4
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        new_index = (c_index + shift) % 52

        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        encryption = encryption + new_character

    elif c and ciphermethod == '6':
        shift = 666
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        new_index = (c_index + shift) % 52

        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        encryption = encryption + new_character

    else:
        encryption += c
        invalid = 1
        break

if invalid != 1:
    print("Cipher chosen:", ciphermethod )

    print("User text:", text)

    print("Encrypted text:", encryption)

