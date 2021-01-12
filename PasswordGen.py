import random
import winclip32

def getPass(n):
    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?')
    password = ''
    for x in range(int(n)):
        spot = random.randint(1, (len(characters)-1))
        password += characters[spot]
    
    return password


if __name__ == '__main__':
    password = getPass(input('Length of password: '))

    winclip32.set_clipboard_data("unicode_std_text", password)

    print(winclip32.get_clipboard_data("unicode_std_text"))