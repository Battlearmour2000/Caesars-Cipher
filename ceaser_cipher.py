
plaintext = input('Enter plaintext, no caps: ')

shift = int(input("Enter shift amount: "))

def ceasar_cipher(plaintext,shift):
    text=''
    for char in plaintext:
        if text == " ":
            text=text+char
        elif char.isupper():
            text = text +chr((ord(char)+ shift-65)%26+65)
        else:
            text = text +chr((ord(char)+ shift-97)%26+97)
    return text

print("Encrypted message is: " ,ceasar_cipher(plaintext, shift))



