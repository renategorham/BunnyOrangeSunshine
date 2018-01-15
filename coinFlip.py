# Coin Flip
#Flips coin 100 times counts faction and run

import random

print("Flip a Coin 100 times.")

flips = 1
tails = 0
heads = 0

while flips < 100:
    coin = random.randint(0,1)
    
    if coin == 0:
        print("T,", end = "")
        tails += 1
        flips +=1
    
    elif coin == 1:
        print("H,", end = "")
        heads += 1
        flips +=1

hRatio = heads / flips
tRatio = tails / flips

print("\n\nNumber of heads is: ", heads, " and porportion of heads is: ", hRatio)
print("Number of tails is: ", tails, " and porportion of tails is: ", tRatio)

input("\n\nPress the enter key to exit.")

