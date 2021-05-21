#  python Guessing_game.py 
import os 
import random 
import math 
#print(os.getcwd())

name =  input("Enter your Name  : ")
print(f"Hello {name} ! Wellcome to Guessing Mania...")

words_list  = ['guessing' , 'keyboard' , "system" , "mouse" ,  "python" ,
               "rates" , "youtube" , "faceboook"  , 'mountains' ,"missile" ,
                "cricket" , "datascience" , "apple" , "sunset" , "macbook"]

index = random.randint(0, len(words_list))
words = words_list[index]

# indexes for the some words to show 
indexes =  random.sample(range(0,len(words)), 3)
guesses = ""
for x in indexes :
    guesses += words[x]
chances = 10

# starter 
play = "yes"


def wanna_play_again():
    global name , play 
    play  = input(f' Hey {name} ,Do you wanna Play again : ( "Yes / No" ) ').lower()
    if play == 'yes':
        global chances , guesses ,words , words_list
        chances = 10 
        index = random.randint(0, len(words_list))
        words = words_list[index]
        indexes =  random.sample(range(0,len(words)), 3)
        guesses = ""
        for x in indexes :
            guesses += words[x]

    else:
        pass 
    

while play == "yes" : 
    while chances > 0 :
        won = True 
        for word in words:
            if word in guesses :
                print(word , end=" ")
            else:
                print("_" , end = " ")
                won = False 

        if won :
            print('\n Congratulatios ..! You Won the Game ..')
            print(f'\n Your got {chances*10} Score .....')
            # ask if you want to play again or not 
            wanna_play_again()
            break 
        
        # take the guess from user
        guess = input("\n Guess the word...")
        guesses += guess

        if guess not in word :
            chances -= 1 

            if chances == 0 :
                print('Sorry , you lose!....')
                # ask you want to play again 
                wanna_play_again()
                break
            
            
            
