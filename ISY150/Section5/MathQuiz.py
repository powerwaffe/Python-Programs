# import for random numbers
import random


# main function
def main():
    # create variables with random values
    number1 = random.randint(0, 999)
    number2 = random.randint(0, 999)
    quiz(number1, number2)


# function for math quiz
def quiz(number1, number2):
    print('Time for some math!')
    print('\t', number1, '\n+\t', number2, '\n__________')
    # actual correct answer
    real_answer = number1 + number2
    # user entered answer
    answer = int(input('\nEnter sum of numbers: '))

    # conditional statements
    if answer == real_answer:
        print('Correct. nice job!')

    else:
        print('Incorrect,', 'the answer is', real_answer)


# call main function
main()
