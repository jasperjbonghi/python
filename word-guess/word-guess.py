import random
from random_word import RandomWords

word_of_the_day = RandomWords().get_random_word()
print("word of the day: " + word_of_the_day)

retry_count = 3
word_bank = ["mauler","objective","rinomilk", "question", "blades", "dinner", "elizabeth"]

word_bank_offset = random.randint(0,len(word_bank)-1)
selected_string = list(word_bank[word_bank_offset])

display_string = [None] * len(selected_string)
string_length = len(selected_string)
for x in range(string_length):
    display_string[x] = '_'

retry_count_string = input("How many retries do you want? : " )
retry_count = int(retry_count_string)
game_won = False
while(retry_count > 0 and game_won is False):
    is_failure = True
    letter = input("please guess the word : " + str(display_string))
    for x in range(0, len(selected_string)):
        letter = letter.lower()
        if(str(letter) == str(selected_string[x])):
            display_string[x] = selected_string[x]
            is_failure = False
            if("_" not in display_string):
                print("you win")
                game_won = True
                break

    if(is_failure):
        retry_count = retry_count-1
        print("you have an error -- tries remaining: " + str(retry_count))

    if (retry_count == 0):
        print("you lose you asshole")

print(selected_string)
