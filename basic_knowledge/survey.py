#!/usr/bin/env python3


class AnonymousSurvey():

    def  __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print("- " + response)


question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

