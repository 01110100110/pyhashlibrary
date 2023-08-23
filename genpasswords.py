import itertools
import hashlib
import os

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]}\|;<.{>,/?`~:;'
maxlength = input("What is the max length\n")
#minlength = input("whats the min length\n")
#minlength = int
correctmaxlen = int(maxlength)+1 #for range only
output_filename = input("Enter the output filename: ")

try:
    # Attempt to open the file in write mode
    with open(output_filename, 'w') as output_file:
        for i in range(1, correctmaxlen):
            combinations = itertools.product(alphabet, repeat = int(maxlength))

            for combo in combinations:
                word = ''.join(combo)
                output_file.write(word + '\n')
        # Print all "Combo's" below maxlength       
        maxlength = int(maxlength) + 1
        print("Output saved to", output_filename)

except FileExistsError:
    # File already exists, append the output to the existing file
    try:
        with open(output_filename, 'a') as output_file:
            combinations = itertools.product(alphabet, repeat = range(abs(correctmaxlen)))

            for combo in combinations:
                word = ''.join(combo)
                output_file.write(word + '\n')

        print("Output appended to", output_filename)
    
    except:
        print("An error occurred while writing to the file.1 ")

#except:
    #print("An error occurred while writing to the file.2")

# Warn the user about the expected size of the library if they choose to use the faster option
try:
    ptextsize = os.path.getsize(output_filename)
    print(f'WARNING. the plaintext file is already {ptextsize} bytes.')

except FileNotFoundError:
    print('invalid file name. VAR_DEBUG: {output_filename} ')

# Scanning proccess type
typeofscan = input("Which method of scanning would you prefer.\n 1. fast scan(requires more temporary storage)\n 2. long scan(takes longer but can be used if you dont have alot of storage)")
if typeofscan == "1" or typeofscan == "fast scan" or typeofscan == "fast":
    print("good so far")

elif typeofscan == "2" or typeofscan == "long" or typeofscan == "longscan":
    print("")

else:
    print("invalid response. ")
