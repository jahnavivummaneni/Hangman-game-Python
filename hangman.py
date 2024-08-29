import random
from wordslst import words
from images import img

def choose_word():
    word=random.choice(words)
    return word.upper()

def game(word):
    res_word="_"*len(word)
    game_over=False
    guessed_letters=[]
    lives=7
    while not game_over:
        guess=input("enter letter").upper()
        if lives<0:
            break
        elif len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("YOU ALREADY GUESSED THIS LETTER")
                print(res_word)
                print(img[lives])
                lives-=1
            elif guess not in word:
                print("THIS LETTER IS NOT IN WORD")
                print(res_word)
                print(img[lives])
                lives-=1
                guessed_letters.append(guess)
            else:
                print("THIS LETTER IS IN WORD")
                word_list=list(res_word)
                for i in range(len(word)):
                    if guess in word[i]:
                        word_list[i]=guess
                res_word="".join(word_list)
                print("WORD=",res_word)
                if "_" not in res_word:
                    game_over=True
                guessed_letters.append(guess)
        else:
            print("NOT A VALID INPUT")
    if game_over:
        print("YOU WON THE GAME")
    else:
        print("YOU RAN OUT LIVES ,AND THE WORD IS",word)
word=choose_word()
print(word)
game(word)
while input("DO YOU WANT TO PLAY?(Y/N)").upper()=="Y":
    word=choose_word()
    print(word)
    game(word)
