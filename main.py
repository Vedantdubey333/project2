'''Program to guess a number if it right or wrong and then calculate the number of guess you have made .'''
import random
Number = random.randint(1,100)
guess = 0
n =-1
while(Number!=n):
    n = int(input("Enter the number :"))
    if (Number<n):
        print("Please Choose a lesser a Number.")
        guess+=1
    elif(Number>n):
        print("Please choose a greater Number.")
        guess+=1
print(f"You have Made the correct guess.\n The Total Number Guess you have made is {guess} ")
with open("highscore.txt","r") as f:
    highscore = f.read()
    if (highscore!=""):
        highscore = int(highscore)
    else:
        highscore = 0
if (highscore<guess): 
    with open("highscore.txt","w") as f1:
        f1.write(str(guess)) 