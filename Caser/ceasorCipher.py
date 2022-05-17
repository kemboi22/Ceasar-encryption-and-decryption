# c= (x-n)%26 <= formula

print("THIS IS CEASAR CIPHER ENCRYPTION AND DECRYPTION ")
chose = int(input("Choose \n 1. To encrypt to ceasar cipher \n 2. To decrypt to normal text"))

if chose == 1:
    text = input("Enter words to be Encrypted: ")
    key = int(input("Enter shift key: "))


    # Create a function for cipher
    def ceasar_cipher_encryption(text, key):
        cipher = ""
        # For loop to loop through the characters of text
        for char in text:
            if char == ' ':  # if there is no character it inserts a blank
                cipher = cipher + char
            elif char.isupper():  # Uppercase letters starts from 65
                cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
            else:  # Lowercase letters  starts from 97
                cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
        return cipher


    print(f"The original text is {text}")
    print(f"The encrypted version is: {ceasar_cipher_encryption(text, key)} ")
elif chose == 2:
    text = input("Enter the text to be decrypted: ")
    key = int(input("The key at which it will be decrypted: "))


    def ceasar_cipher_decryption(text, key):
        decrypted = ''
        for char in text:
            if char == ' ':
                decrypted = decrypted + char
            elif char.isupper():
                decrypted = decrypted + chr((ord(char) - key))
            else:
                decrypted = decrypted + chr((ord(char) - key))
        return decrypted


    print(f"The encrypted text {text}")
    print(f"The decrypted text is {ceasar_cipher_decryption(text, key)}")
