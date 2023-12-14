# your code goes here!
import time

def countdown (sec):
    while sec > 0:
        print(f'{sec} SECOND(S)!')
        countdown_with_sleep(sec)
        sec = sec - 1
    print('HAPPY NEW YEAR!')
    

def countdown_with_sleep(sec):
    time.sleep(1)

