# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Jack Utzerath
#Program 3
#this is my program with help wikipedia on the cipher

def key(message, secretWord):
    word = list(secretWord)
    key = []

    #for loop to ensure the key is as long as the message
    #if message: Hello
    #and the key: calc
    #then we have to loop back the word so that key is as long as the message
    #the key should be: calcc

    for i in range(0, len(message)):
        #if i > message then we should mod word to get the next char
        key.append(word[i % len(word)])

    return (key)

def encode(message, key):
    cipher = []

    for i in range (0, len(message)):
        if (message[i] == " " ) or (message[i] == "'" ) or (message[i] == "."):
            cipher.append(message[i])
        else:
            #we have create a starting point to encode
            #lets get the index of A
            encode = ord('A')
            #this get the int of the letter A that is stored in python

            #now we have to use to the Vigenere Cipher equation to encode
            # (message + key) mod 26
            encode += (ord(message[i]) + ord(key[i])) % 26

            # convert index int (encode) to char and add it to the list
            cipher.append(chr(encode))

    return(cipher)

def decode(cipher, key):
    text = []
    for i in range(0, len(cipher)):
        if (message[i] == " " ) or (message[i] == "'" ) or (message[i] == "."):
            text.append(message[i])
        else:
            # we should create a starting point to decode
            # lets get the index of A
            decode = ord('A')
            # this get the int of the letter A that is stored in python

            # now we have to use to the Vigenere Cipher equation to decode
            # ((message - key) + 26) mod 26
            decode += (ord(cipher[i]) - ord(key[i]) + 26) % 26

            #convert index int (decode) to char and add it to the list
            text.append(chr(decode))


    return(text)

if __name__ == '__main__':

    message = "it's hardware that makes a machine fast. it's software that makes a fast machine slow."
    secretWord = "Apple"

    #get the key
    key = key(message.upper(), secretWord.upper())

    #use encode message
    cipher = encode(message.upper(), key)

    #use decode message
    text = decode(cipher, key)

    #prints the message
    print("Orginal text... ")
    print(message)
    print()
    #prints out the key
    print("Key... ")
    for i in range(0, len(key)):

        print(key[i].lower(), end= "")

    #print our the encoded message
    print()
    print()
    print("Encoded text... ")
    for i in range(0, len(cipher)):
        print(cipher[i].lower(), end= "")

    #print out the decoded message
    print()
    print()
    print("Decoded text... ")
    for i in range(0, len(text)):
        print(text[i].lower(), end="")

    print()





