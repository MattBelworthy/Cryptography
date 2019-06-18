def getMode():
    while True:
        mode = input('encrypt mode ("e") or decrypt mode ("d"):\n')
        if mode[0] in 'e d'.split():
            return mode
        else:
            print('Enter either "encrypt" ("e") or "decrypt" ("d").')

def getText():
    print('Enter your Text:')
    return input()

def getKey():
    key = 0
    while True:
        key = input('Enter the key number (1 >=< 26):\n')
        if (int(key) >= 1 and int(key) <= 26):
            return int(key)

def getCipherText(mode, text, key):
    ciphered = ''
    if mode[0] == 'd':
        key = -key

    for symbol in text:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num <ord('a'):
                    num += 26

            ciphered += chr(num)
        else:
            ciphered += symbol
    return ciphered

def main():
    mode = getMode()
    message = getText()
    key = getKey()

    print('Your translated text is:')
    print(getCipherText(mode, message, key))
main()
