import datetime

text = input("Welcome to the second release of Pysoteric! Enter a string of text to be encrypted \n")

encryption = ""

invalid = 0

ciphermethod = input("Now enter a cipher method to be used. 3 for 3 shift (weakest), 4 for 4 shift(stronger) or 6 "
                     "for the sixer cipher(strongest) \n")

for c in text:
    if c and ciphermethod == '3':
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + int(ciphermethod))
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    elif c and ciphermethod == '4':
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + int(ciphermethod))
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    elif c and ciphermethod == '6':
        # gets unicode value of the current character of input
        c_unicode = ord(c)
        # appends the shift to the character index
        c_unicode = (c_unicode + int(ciphermethod))
        # encryption variable stores the now encrypted text
        encryption += chr(c_unicode)

    else:
        invalid = 1

if invalid != 1:
    print("Cipher chosen:", ciphermethod)

    print("User text:", text)

    print("Encrypted text:", encryption)

    savechoice = input("Write Result to a txt file?(y/n)")

    if savechoice.lower() == "y":
        # opens text file for writing
        f = open("results.txt", "a")
        # grabs the current date
        dnow = datetime.datetime.now()
        # formats the date to an array of strings for displaying (month day and year format)
        datedis = dnow.strftime("%B"), dnow.strftime("%d"), dnow.strftime("%Y")

        f.write(str(datedis))

        f.write("\nEncrypted text: ")

        f.write(encryption)

        f.write("\n")

        f.close()

        print("Encrypted text has been saved to 'results.txt'")
