from datetime import datetime
import random
import time

odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,]

for ch in "Hi!":
     print(ch)

for x in range(5):
    right_this_second = datetime.today().second
    if right_this_second in odds:
        print("this minute seems a little odd.")
    else:
        print("its even")
    sleep_time = random.randint (0,5)
    time.sleep(sleep_time)
word_bank[44]
