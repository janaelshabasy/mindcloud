import random
print("Welcome player")
print("I'm thinking of a number between 1 and 100")
print("You have 6 attempts to guess it")
score=0
rounds=0
roundswon=0
while True:
    number=random.randint(1, 100)
    rounds+=1
    points=0
    i=1
    remain=6
    while True:
        if i<=6:
         remain-=1
         print("Attempt ",i,"/6")
         guess= int(input("Enter your guess "))
         if guess==number:
            print("Congratulations!")
            print("You guessed the number")
            points+=1
            roundswon+=1
            break
         elif guess<number:
            if number-guess>5:
             print("Too low")
            else:
             print("Higher")
         elif guess>number:
            if guess-number>5:
             print("Too high")
            else:
             print("Lower")
        else:
         break
        i+=1
    points+=remain
    score+=points
    print("Guesses remaining: ",remain)
    print("Points earned: ",points)
    print("Current score: ",score)
    play=input("Play another round? (y/n) ")
    if play!="y":
     break
print("Rounds played: ",rounds)
print("Rounds won: ",roundswon)
print("Final score: ",score)
