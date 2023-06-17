'''
Description: This program lets a child practice arithmetic skills. The program should first ask
             for what kind of practice is wanted: addition(1), subtraction(2), or multiplication(3).
             Then the program will have to loop for each of the desired operations that lets the user
             repeat the practice as many times as desired. Two random numbers will be generated
             (0-9), and the child will have to add, subtract or multiply them. If the child answers
             the question correctly, congradulate them, and give them two different number to try.
             If the child answers incorrectly, the problem should be repeated (with the two same numbers).
'''

import random

answer = int(input("Would you like to add(1), subtract(2) or multiply(3)? "))
play = 1

while play == 1:
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    while answer != 1 and answer != 2 and answer != 3:
            answer = int(input("Please enter a valid option! To add(1), subtract(2) or multiply(3): "))

    if answer == 1:
        answerAddition = int(input("What is " + str(a) + " + " + str(b) + " equal to: "))

        while answerAddition != addition:
            answerAddition = int(input("That is incorrect, what is " + str(a) + " + " + str(b) + " equal to: "))

        if answerAddition == addition:
            print("That is correct!")
            
    elif answer == 2:
        answerSubtraction = int(input("What is " + str(a) + " - " + str(b) + " equal to: "))

        while answerSubtraction != subtraction:
            answerSubtraction = int(input("That is incorrect, what is " + str(a) + " - " + str(b) + " equal to: "))

        if answerSubtraction == subtraction:
            print("That is correct!")
            
    elif answer == 3:
        answerMultiplication = int(input("What is " + str(a) + " * " + str(b) + " equal to: "))

        while answerMultiplication != multiplication:
            answerMultiplication = int(input("That is incorrect, what is " + str(a) + " * " + str(b) + " equal to: "))

        if answerMultiplication == multiplication:
            print("That is correct!")

    play = int(input("Would you like to try again? (1 for Yes, 2 for No): "))

    while play != 1 and play != 2:
        print("Please enter a valid option!")
        play = int(input("Would you like to try again? (1 for Yes, 2 for No): "))

    if play == 1:
        answer = int(input("Would you like to add(1), subtract(2) or multiply(3)? "))
    if play == 2:
        print("Thank you for playing!")