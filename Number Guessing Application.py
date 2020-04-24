


import random
# Welcome
def randomNumber():
    print("Welcome, you can start to play your game, goodluck to you ")
    guess_level = input("Choose Difficulty, Enter Easy, Medium or Hard: ").upper()
    return guess_level

    guess = 0

    guesses = 0

    Chances = 0

    levels = ""

    Result = ""

    x = 25;

    choose = 0;
    print("Pls enter your guess number");
    choose = int.Parse(input());
    if (choose == x):
         print("You guessed right")

    else:
     print("You guessed wrong")
     print("Now you have to choose between three levels")
     print("Press 1 for easy")
     print("Press 2 for medium")
     print("Press 3 for hard")



     Inputs = int.Parse(input())

    if (Inputs == 1):
     levels = "Easy"

     if (Inputs == 2):
      levels = "Medium"

     if (Inputs == 3):

      levels = "Hard"

     else:

      Result = "Game Over";

    if (levels == "Easy"):
     randomNumber = random.Next(1, 11)
    chances = 6

    print(guesses(1, 10, chances, randomNumber, guess))
    if (levels == "Medium"):
     randomNumber = random.Next(1, 21)
    chances = 4

    print(guesses(1, 20, chances, randomNumber, guess))
    if (levels == "Hard"):
     randomNumber = random.Next(1, 51);
    chances = 3

    print(guesses(1, 50, chances, randomNumber, guess));

    print(Result);

    
    while (Guesses != RandomNumber):

        if Chances > 1:

            print(f"You have {Chances} chances left.")
        print(f"Guess the number between {minVal} and {maxVal}: ")
        Guesses = int.Parse(input());

        if (Chances == 1):

         print(f"You have {Chances} chance left.")
        print(f"Guess the number between {minVal} and {maxVal}: ")
        Guesses = int.Parse(Console.ReadLine())
        if (Guesses == RandomNumber & Chances > 0):

         Output = f"You are right, the answer is {RandomNumber}"
        break


        if (Chances == 1):

         Output = "You no longer have any chances, Game Over";
        break
    else :
     print("You guessed wrong");

     Chances -= 1
     return Output;







