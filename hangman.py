#      - - - - - - - - - - - - - - - HANGMAN GAME - - - - - - - - - - - - - -


#libraries
import random
import time

# Introduction Program
print("\n~ ~ ~ Welcome To Hangman Game ~ ~ ~\n")
name=input("Enter Your Name:")
print("Hello "+name+"! Best of luck!")
time.sleep(1)
print("3..",end="")
time.sleep(1)
print("2..",end="")
time.sleep(1)
print("1",end=" ")
time.sleep(1)
print("Let's Play Hangman")

# main
def main():
    global count
    global display
    global meaning
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess =  {
"annoy":"Making someone angry"
,"calm": "Free of any disturbance"
,"consequences": "An unpleasant or unwelcome result of an action"
,"decide": "Choose out of several alternatives"
,"discover": "Find something unexpectedly or during a search."
,"enormous":"Something big or huge"
,"explore": "Learn about something or inquire about a subject in detail."
,"grumpy": "Someone who is bad-tempered and irritable"
,"ignore": "Fail to consider something important"
,"investigate": "Carry out an inquiry to discover and examine facts to establish the truth"
,"jealous": "Feeling protective of one’s right or possession"
,"leader": "An individual who commands a group, country, or an organization"
,"lovely": "Extremely beautiful or attractive"
    }
    word,meaning = key, val = random.choice(list(words_to_guess.items()))
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# Loop to Execute Game Again
def play_loop():
    global play_game
    play_game=input("Do You Want to play again? y = YES, n = NO \n")
    while play_game not in ["y","n","Y","N"]:
        play_game=input("Do You Want to play again? y= YES, n= NO \n")
    if play_game == "y" or play_game == "Y":
        main()
    elif play_game == "n" or play_game == "N":
        print("Thanks For Playing! We Expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global meaning
    global already_guessed
    global play_game
    limit = 5
    already=[]
    guess = input("This is the Hangman word: "+display+"\nMeaning Of Word:"+meaning+"\nEnter Your Guess:")
    guess = guess.strip()
    already.append(guess)
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input,Enter Only One Letter "+name+"\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try Another Letter\n")

    else:
        count +=1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess.Guesses remaining"+ str(limit - count) +"\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess.Guesses remaining"+str(limit - count) +"\n")


        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess.Guesses remaining"+str(limit - count) +"\n")


        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess.Guesses remaining" + str(limit - count) + "\n")
        elif count==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()


    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()