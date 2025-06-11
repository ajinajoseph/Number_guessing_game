import random
print("welcome to number guessing game!!")
print("You have 10 chances to guess the number.Let's Start\n")
low=int(input("enter the lower bound:"))
high=int(input("enter the higher bound:"))
print(f"\nYou have 10 chances to guess the number between {low} and {high}. Let's start!")
num=random.randint(low,high)
ch=10
gc=0
while gc<ch:
    gc+=1
    guess=int(input("enter your guess:"))
    if guess==num:
        print(f"\nyour guess is correct,the number is {num},you guessed it in attempt {gc}.")
    elif guess<num:
        print("Too low,Try a higher number.")
    else:
        print("Too high,Try a lower number.")
if guess!=num:
     print(f"Your number of chance is over .\nThe number was {num},Better luck next Time.")
