def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char == ' '):
            result+=char
        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))
print ("PT  : " + plaintext)
print ("Shift : " + str(key))
print ("CT: " + encrypt(plaintext,key))
