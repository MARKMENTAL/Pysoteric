text = input("Welcome to the second release of Pysoteric! Enter a string of text to be encrypted \n")

encryption = ""

invalid = 0

ciphermethod = input("Now enter a cipher method to be used. 3 for caesar based(weakest), 4 for 4 shift(stronger) or 6 "
                     "for the sixer cipher(strongest) \n")

for c in text:
    if c and ciphermethod == '3':
        shift = 3
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + shift)
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    elif c and ciphermethod == '4':
        shift = 4
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + shift)
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    elif c and ciphermethod == '6':
        shift = 6
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + shift)
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    else:
        encryption += c
        invalid = 1
        break

if invalid != 1:
    print("Cipher chosen:", ciphermethod)

    print("User text:", text)

    print("Encrypted text:", encryption)
