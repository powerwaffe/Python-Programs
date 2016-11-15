# main function
def main():
    print('-------------------Calculate your Test Score----------------\n')
    print('Please enter five test scores, press ENTER after each value:')
    # prompt user to enter five test scores
    score1 = int(input('Score one: '))
    score2 = int(input('Score two: '))
    score3 = int(input('Score three: '))
    score4 = int(input('Score four: '))
    score5 = int(input('Score five: '))
    # call function
    calc_average(score1, score2, score3, score4, score5)


# function for calculating average
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    # print table
    # call function to return letter grade
    print('Score\tNumeric Grade\tLetter Grade')
    print('----------------------------------')
    print('score1:\t\t  ', score1, '\t\t', determine_grade(score1))
    print('score2:\t\t  ', score2, '\t\t', determine_grade(score2))
    print('score3:\t\t  ', score3, '\t\t', determine_grade(score3))
    print('score4:\t\t  ', score4, '\t\t', determine_grade(score4))
    print('score5:\t\t  ', score5, '\t\t', determine_grade(score5))
    # print average
    print('-----------------------------------')
    print('Average score ', average, '\t', determine_grade(average))


# function for determining letter grade
def determine_grade(score):
    letter_grade = score

    # conditional statement for letter grade
    if letter_grade >= 90:
        return "A"
    elif 80 <= letter_grade <= 89:
        return "B"
    elif 70 <= letter_grade <= 79:
        return "C"
    elif 60 <= letter_grade <= 69:
        return "D"
    else:
        return "F"


# call main function
main()
