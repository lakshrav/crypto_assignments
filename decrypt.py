def decrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char == ' '):
            result+=char
        elif (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

ciphertext = input("Enter ciphertext: ")
key = int(input("Enter key: "))
print ("CT  : " + ciphertext)
print ("Shift : " + str(key))
print ("PT : " + decrypt(ciphertext,key))
