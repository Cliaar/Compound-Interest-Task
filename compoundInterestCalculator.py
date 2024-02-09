import math
from calculator import compoundInterestCalculator
import os

running = True
while(running == True):
    try:
        print("To calculate the time it will take to reach a target amount, press enter. To exit, type 'exit'")
        userInput = input("input: ")
        if userInput != 'exit' and userInput != '':
            raise Exception
        if userInput == 'exit':
            running = False
        else:
            try:
                # Deposit input
                deposit = int(input("Enter deposit amount ($): "))
                if deposit < 1:
                    raise ValueError()
                # Interest input
                interest = float(input("Enter interest rate (%): "))
                if interest <= 0:
                    print('Multiplication factor must be greater than 0')
                    raise Exception
                # Multiplication factor input
                multiplicationFactor = float(input("Enter multiplication factor: "))
                if multiplicationFactor < 1:
                    raise ValueError()
                # Calculate time
                years = compoundInterestCalculator(deposit, interest, multiplicationFactor)
                print("It will take %d year(s) to reach $%.2f" % (years, deposit * multiplicationFactor))
                input('press enter to continue')
                os.system('cls')
            except ValueError:
                print('Please enter a number greater or equal than 1 without symbols')
                input('press enter to continue')
                os.system('cls')
            except:
                print("An error occurred. Please try again.")
                input('press enter to continue')
                os.system('cls')
    except:
        print("An error occurred. Please try again.")
        input('press enter to continue')
        os.system('cls')
