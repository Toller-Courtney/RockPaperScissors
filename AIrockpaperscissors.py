from random import choice
import time

#This is starting our scors at 0 for the user and the computer
userScore=0
compScore=0

# these are the choices and results its saying the first element is beaten by the second element
choices= {"r":"p", "s":"r", "p":"s"}

#Here we are saything the previous choices could be rock, paper, or scissors
previous=["r", "p", "s"]

#This is starting our rounds and the counting them up to 6
rnd=1

#Here is the block of code that is going to determine the results of each round.
while True:
    print("Round: ",rnd)
    userOption=input("Do you choose (r)ock, (s)cissors, or (p)aper?")
    compOption= choices[choice(previous)]
    
    print ("Computer chose: ", compOption)
    
    if len(userOption)==0:
        print("Invalid anser, please try again")
        time.sleep(1)
        continue
    
    elif userOption[0].lower()==compOption:
        #this is going to take in to account what the users previous selection was and the computer is goin
        #to use the to determine what the next move will be. It's collecting the patterns of the users selection.
        previous.append(userOption)
        print("Draw")
        time.sleep(1)
        continue
    
    elif userOption[0].lower()=="r" and compOption=="s":
        previous.append(userOption)
        print("User wins this round")
        time.sleep(1)
        userScore=userScore+1
    elif userOption[0].lower()=="p" and compOption=="s":
        previous.append(userOption)
        print("Computer wins this round")
        time.sleep(1)
        compScore=compScore+1
    elif userOption[0].lower()=="s" and compOption=="p":
        previous.append(userOption)
        print("User wins this round")
        time.sleep(1)
        userScore=userScore+1
    elif userOption[0].lower()=="r" and compOption=="p":
        previous.append(userOption)
        print("Computer wins this round")
        time.sleep(1)
        compScore=compScore+1
    elif userOption[0].lower()=="s" and compOption=="r":
        previous.append(userOption)
        print("Computer wins this round")
        time.sleep(1)
        compScore=compScore+1
    elif userOption[0].lower()=="p" and compOption=="r":
        previous.append(userOption)
        print("User wins this round")
        time.sleep(1)
        userScore=userScore+1
    else:
        print("Invalid answer, please try again")
        continue

# here we are counting up the rounds that have already been played. When it gets to 6 the computer will stop
#add up how many rounds the user and computer each one and then who wins the game based on number of rounds won.
    rnd=rnd+1
    if rnd==6:
        break

print("User Won ", userScore)
print("Computer Won ", compScore)

if userScore >compScore:
    print("User wins the game!")
elif compScore>userScore:
    print("Computer wins the game!")
else:
    print ("Draw!")
