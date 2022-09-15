choice=int(input(' Choose 1 to encrypt a message: \n Choose 2 to decrypt a message:'))
#user chooses whether they want to encrypt a message or decrypt one

if choice == 1:

    plaintext = input('Enter plaintext: ')
    shift = int(input("Enter shift amount: "))

    def ceasar_cipher_enc(plaintext,shift):
        text=''
        for char in plaintext:
            if text == " ":
                text=text+char
            elif char.isupper():
                text = text +chr((ord(char)+ shift-65)%26+65)
            else:
                text = text +chr((ord(char)+ shift-97)%26+97)
        return text


    print("Encrypted message is: " ,ceasar_cipher_enc(plaintext, shift))
    
elif choice ==2:

    gibber = input('Enter message: ')
    shift = int(input("Enter shift amount: "))

    def ceasar_cipher_dec(gibber,shift):
        text=''
        for char in gibber:
            if text == " ":
                text=text+char
            elif char.isupper():
                text = text +chr((ord(char)- shift-65)%26+65)
            else:
                text = text +chr((ord(char)- shift-97)%26+97)
        return text

    print("Dencrypted message is: " ,ceasar_cipher_dec(gibber, shift))
else:
    print('Please make a correct choice')
