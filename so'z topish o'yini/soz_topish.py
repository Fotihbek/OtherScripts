from uzwords import words
import random

def getwords():
    global word
    word = random.choice(words)
    global a
    a = len(word)
    print(f'{a} xonali so\'z o\'yladim, topa olasizmi?')

def checkword():
    list = []
    site = '-'*a
    
    while True:
        
        if word != site:
            letter = input('Harf kiriting - ').lower()
            if letter not in site:
                list.append(letter)
                if letter in word:
                    for i in range(len(word)):
                        if i == len(word):
                            print(site)
                            break
                        elif word[i] == letter:
                            site = site[:i] + word[i] + site[i+1:]
                else:
                    print('Xato, boshqa harf kiriting! Siz kiritgan harflar -', list)
            else:
                print('Bu harfni kiritgansiz, qaytadan!', list)    
            print(site)        
        else:
            print('Tabriklayman!', len(list), 'urunishda topdingiz')
            break

          
        
getwords()
checkword()



