import random


class Question(object):
    # static variables for scores
    score1 = 0
    score2 = 0

    def __init__(self, question, answer, solution):
        self.__question = question
        self.__answer = answer
        self.__solution = solution

    def set_question(self, question):
        self.__question = question

    def get_question(self):
        return self.__question

    def set_answer(self, answer):
        self.__answer = answer

    def get_answer(self):
        return self.__answer

    def set_solution(self, solution):
        self.__solution = solution

    def get_solution(self):
        return self.__solution

    # ask player 1 questions
    def ask1(self):
        print(self.get_question() + "?")
        for n, option in enumerate(self.get_solution()):
            print("%d) %s" % (n + 1, option))

        # take user as integers
        response = int(input())

        if response == self.get_answer():
            print("CORRECT")
            Question.score1 += 1
        else:
            print("Wrong...")

    # ask player 2 questions
    def ask2(self):
        print(self.get_question() + "?")
        for n, option in enumerate(self.get_solution()):
            print("%d) %s" % (n + 1, option))

        # take user input as integers
        response = int(input())

        if response == self.get_answer():
            print("CORRECT")
            Question.score2 += 1
        else:
            print("Wrong...")

# create list of questions
questions = [
    Question('How many days are in a ' + \
             'lunar year?', 1, ['354', '365', \
                                '243', '379']),
    Question('What is the largest planet?', 2, \
             ['Mars', 'Jupiter', 'Earth', \
              'Pluto']),
    Question('What is the largest kind of ' + \
             'whale?', 4, ['Orca whale', \
                           'Humpback whale', \
                           'Beluga whale', 'Blue whale']),
    Question('Which dinosaur could fly?', 3, \
             ['Triceratops', 'Tyranosaurus Rex', \
              'Pteranodon', 'Diplodocus']),
    Question('Which of these Winnie the Pooh ' + \
             'characters is a donkey?', 2, \
             ['Pooh', 'Eeyore', 'Piglet', \
              'Kanga']),
    Question('What is the hottest planet?', 4, \
             ['Mars', 'Pluto', 'Earth', \
              'Venus']),
    Question('Which dinosaur had the ' + \
             'largest brain compared to body' + \
             ' size?', 1, ['Troodon', 'Stegosaurus', \
                           'Ichthyosaurus', 'Gigantoraptor']),
    Question('What is the largest type ' + \
             'of penguins?', 3, \
             ['Chinstrap penguins', \
              'Macaroni penguins', \
              'Emperor penguins', \
              'White-flippered penguins']),
    Question("Which children's story " + \
             'character is a monkey?', 2, \
             ['Winnie the Pooh', \
              'Curious George', 'Horton', \
              'Goofy']),
    Question('How long is a year on Mars?', 4, \
             ['550 Earth days', \
              '498 Earth days', \
              '126 Earth days', \
              '687 Earth days'])]

# randomizes the order of the questions
random.shuffle(questions)

print('It is trivia time!!!\nThis is a two player game, each player must answer 5 questions')

# player 1's turn
print("Player 1's turn\n")
for question in questions[0:5]:  # in range 5
    # call player one method
    question.ask1()

# player 2's turn
print("\n\nPlayer 2's turn, answer 5 questions!")
for questions in questions[5:10]:
    # call player 2 method
    questions.ask2()

# print scores
print("Player 1's score: ", Question.score1, "\nPlayer 2's score: ", Question.score2)

# check who the winner is, or if there is a tie
if Question.score1 > Question.score2:
    print("Player 1 wins!")
elif Question.score1 < Question.score2:
    print("Player 2 wins!")
else:
    print("Tie")
