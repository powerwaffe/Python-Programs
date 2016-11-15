# Programming Exercise 10-8


class Question:
    def __init__(self, question, answer1, answer2, \
                 answer3, answer4, solution):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__solution = solution

    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_solution(self, solution):
        self.__solution = solution

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_solution(self):
        return self.__solution

    def __str__(self):
        result = self.get_question() + '\n' + \
                 '1. ' + self.get_answer1() + '\n' + \
                 '2. ' + self.get_answer2() + '\n' + \
                 '3. ' + self.get_answer3() + '\n' + \
                 '4. ' + self.get_answer4()
        return result

    def isCorrect(self, answer):
        return answer == self.get_solution()


def get_questions():
    question = Question()
    questions = []

    # Create questions and add to list.
    question1 = question.Question('How many days are in a ' + \
                                  'lunar year?', '354', '365', \
                                  '243', '379', 1)
    questions.append(question1)
    question2 = question.Question('What is the largest planet?', \
                                  'Mars', 'Jupiter', 'Earth', \
                                  'Pluto', 2)
    questions.append(question2)
    question3 = question.Question('What is the largest kind of ' + \
                                  'whale?', 'Orca whale', \
                                  'Humpback whale', \
                                  'Beluga whale', 'Blue whale', 4)
    questions.append(question3)
    question4 = question.Question('Which dinosaur could fly?', \
                                  'Triceratops', 'Tyranosaurus Rex', \
                                  'Pteranodon', 'Diplodocus', 3)
    questions.append(question4)
    question5 = question.Question('Which of these Winnie the Pooh ' + \
                                  'characters is a donkey?', \
                                  'Pooh', 'Eeyore', 'Piglet', \
                                  'Kanga', 2)
    questions.append(question5)
    question6 = question.Question('What is the hottest planet?', \
                                  'Mars', 'Pluto', 'Earth', \
                                  'Venus', 4)
    questions.append(question6)
    question7 = question.Question('Which dinosaur had the ' + \
                                  'largest brain compared to body' + \
                                  ' size?', 'Troodon', 'Stegosaurus', \
                                  'Ichthyosaurus', 'Gigantoraptor', 1)
    questions.append(question7)
    question8 = question.Question('What is the largest type ' + \
                                  'of penguins?', \
                                  'Chinstrap penguins', \
                                  'Macaroni penguins', \
                                  'Emperor penguins', \
                                  'White-flippered penguins', 3)
    questions.append(question8)
    question9 = question.Question("Which children's story " + \
                                  'character is a monkey?', \
                                  'Winnie the Pooh', \
                                  'Curious George', 'Horton', \
                                  'Goofy', 2)
    questions.append(question9)
    question10 = question.Question('How long is a year on Mars?', \
                                   '550 Earth days', \
                                   '498 Earth days', \
                                   '126 Earth days', \
                                   '687 Earth days', 4)
    questions.append(question10)

    return questions


def main():
    my_questions = get_questions()
    questions = Question.get_question(my_questions.index(0), my_questions.index(1))


main()
