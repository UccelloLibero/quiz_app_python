import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)

        # Generate 10 random questions with numbers from 1 to 10
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)

            # Add these questions into self.questions
            self.questions.append(question)

    def take_quiz(self):
        # Log the start time
        self.start_time = datetime.datetime.now()

        # Ask all of the questions
        for question in self.questions:
            # Log if they got the questions right
            self.answers.append(self.ask(question))
        else:
            # Log the end time
            self.end_time = datetime.datetime.now()

        # Show a summary
        return self.summary()

    def ask(self, question):
        correct = False # By defult they got the question wrong

        # Log the start time
        question_start = datetime.datetime.now()

        # Capture the answer
        answer = input(question.text + " = ")

        # Check the answer
        if answer == str(question.answer):
            correct = True

        # Log the end time
        question_end = datetime.datetime.now()

        # If the answer is right, send back True
        # Otherwise send back False
        # Send back the elapsed time, too
        return correct, question_end - question_start

    def total_correct(self):
        # Return the total number of corect answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # Print how many you got right and the total number or questions, e.g 5/10
        print("You got {} out of {} correct.".format(self.total_correct(), len(self.questions)))

        # Print the total time for the quiz: e.g. 30 seconds!
        print("It took you {} seconds total to finish the quiz!".format((self.end_time - self.start_time).seconds))


Quiz().take_quiz()

# Change the app so it takes a number of questions to generate
# Make sure the user can specify the range they want the numbers to come from
# Add in some further stats thet tell you how long it took to answer each question
