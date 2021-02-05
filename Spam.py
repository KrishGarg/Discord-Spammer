import pyautogui
import time

#declaring variables
looper = 0 
msgs = 0

timeneeded = int(input("Time you need to switch to discord (in seconds): "))
messages = int(input("How many messages per cycles: "))
cycles = int(input("How many cycles of messages: "))
text = input("What you want to spam: ")
print("Quickly, you have", timeneeded, "seconds to open discord and the channel/dm you want to spam in!")

def spam():                       #I mean if you don't understand even this, duh.
    pyautogui.typewrite(text)
    pyautogui.press("enter")

#gives time to switch to discord
time.sleep(timeneeded)

while looper < cycles:            #change the integer to the number of times you want to do 5-message cycles
    while msgs < messages:        #how many messages per cycles
        spam()                    #spam :evil:
        msgs+=1                   #to actually end 1 cycle 
    time.sleep(3)                 #time break between cycles to prevent limiting by discord
    msgs=0                        #resetting the cycle
    looper+=1                     #increasing the looper variable to limit the repeatations