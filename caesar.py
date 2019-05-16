#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:        #select decryption or encryption based off input
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message: ')      #takes message from user
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())                                        #takes key and stores it as key
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key         #if decrypting key isnegative , reverse shift
    translated = ''           #empty string

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol    #adds it into the empty string
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):        #
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()     #calling the previously defined functions
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))      #returns the user the string