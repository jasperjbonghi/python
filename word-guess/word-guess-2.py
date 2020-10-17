import random
from os import system, name

retry_count = 3
GAME_WON = 2
GUESS_SUCCESS = 0
GUESS_FAILED = 1

def get_random_word():
    word_bank = ["mauler","objective","rinomilk", "question", "blades", "dinner", "elizabeth"]
    word_bank_offset = random.randint(0,len(word_bank)-1)
    selected_string = list(word_bank[word_bank_offset])
    return selected_string

def get_blank_display_word():
    display_string = [None] * len(selected_string)
    string_length = len(selected_string)
    for x in range(string_length):
        display_string[x] = '_'
    return display_string

def get_retry_count():
    retry_count_string = input("How many retries do you want? : " )
    retry_count = int(retry_count_string)
    return retry_count

def update_status(state,retry_count):
    if(state == GUESS_FAILED):
        retry_count = retry_count-1
        print("you have an error -- tries remaining: " + str(retry_count))
    if (retry_count == 0):
        print("you lose you asshole")

    update_display(retry_count)
    return retry_count

def update_display(retry_count):
    system("cls")

    print("_||_______________")
    print(" ||            |")

    if(retry_count == 0):
        print(" ||            O")
        print(" ||          __|__")
        print(" ||            |")
        print(" ||            |")
        print(" ||           / \\")
    elif(retry_count == 1):
        print(" ||            O")
        print(" ||          __|__")
        print(" ||            |")
        print(" ||            |")
    elif(retry_count == 2):
        print(" ||            O")
        print(" ||          __|__")
        print(" ||            |")
    elif(retry_count == 3):
        print(" ||            O")
        print(" ||            |")
    elif(retry_count == 4):
        print(" ||            O")

    for x in range(retry_count + 3):
        print(" ||")

    print("_||_______________")


def prosses_guess(display_string, selected_string):
    state = GUESS_FAILED
    letter = input("please guess the word : " + str(display_string)).lower()
    for x in range(0, len(selected_string)):
        if(str(letter) == str(selected_string[x])):
            display_string[x] = selected_string[x]
            state = GUESS_SUCCESS
            if("_" not in display_string):
                print("you win")
                state = GAME_WON
    return state
#----------------------------------------------------
system("cls")

selected_string = get_random_word()

display_string = get_blank_display_word()

retry_count = get_retry_count()

while(retry_count > 0):
    state = prosses_guess(display_string, selected_string)
    if (state == GAME_WON):
        break
    retry_count = update_status(state, retry_count)

print(selected_string)
