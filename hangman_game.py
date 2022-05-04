#kullanılan harfler var bunları tekrar kullanamaz harfi bulursa buldun dicek - ler olcak yerine gelcek
from word import words
import random
import string

def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def main():
    word = get_word(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6

    while len(wordLetters) > 0 and lives > 0:
        
        word_list = [letter if letter in usedLetters else "-" for letter in word] 
        
        print("Used Letters:", " ".join(sorted(usedLetters)), "Lives: ", lives)
        print(f"Current Word: ", " ".join(word_list))
        
        userLetter = input("Guess a letter: ").upper()
        
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1
                print("You guessed wrong letter.")
                
        elif userLetter in usedLetters:
            print("You have already used the letter")
        else:
            print("Invalid character")
    
        
    if lives == 0:
        print(f"You lose. Word was {word}")
    else:
        print(f"You win. Word was {word}")

    
main()



