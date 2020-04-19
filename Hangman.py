import sys

guessedletters=[]
guessesleft=10

def guess():
    global word,guessedletters,guessesleft
    print()
    printables=""
    for letter in word:
        if letter[1]==0 and letter[0].isalpha():
            printables+="_"
        else:
            printables+=letter[0]
    print(printables)
    if "_" not in printables:
        print("You win!")
        sys.exit()
    print("You have "+str(guessesleft)+" wrong guesses left.")
    print("You have already guessed: "+(", ".join([chr(lett) for lett in guessedletters])))
    choice=input("Choose a letter")
    if choice.upper() in [chr(i) for i in range(65,91)]:
        if choice.upper() in guessedletters:
            print("You've already guessed that")
            guess()
        else:
            guessedletters.append(ord(choice.upper()))
            guessedletters.sort()
            if choice.upper() in [letter[0].upper() for letter in word]:
                for letter in word:
                    if choice.upper()==letter[0].upper():
                        letter[1]=1
            elif guessesleft==1:
                print("You lose. The word was "+(("").join([letter[0] for letter in word])))
                sys.exit()
            else:
                guessesleft-=1
                print("You are wrong")
    else:
        print("You need to input a letter")
    guess()
    
word=[[letter,0] for letter in input("What is the secret word?")]
[print() for i in range(54)]
guess()
