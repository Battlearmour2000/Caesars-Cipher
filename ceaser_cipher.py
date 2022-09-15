
plaintext = input('Enter plaintext: ')
#this var will hold the text to be encrypted

shift = int(input("Enter shift amount: "))
#this will hold the amount of shift

def caesar_cipher(plaintext,shift):
    #created a function
    text=''
    # local var to hold each character in the loop
    for char in plaintext:
        if text == " ":
            text=text+char
            #skips any blank spaces and avoids encrypting
        elif char.isupper():
            text = text +chr((ord(char)+ shift-65)%26+65)
            #encrypts uppercase letters
        else:
            text = text +chr((ord(char)+ shift-97)%26+97)
            #encrypts lower case letters
    return text

print("Encrypted message is: " ,caesar_cipher(plaintext, shift))
#recalled function and display output



