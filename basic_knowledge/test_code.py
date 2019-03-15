#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name
from survey import AnonymousSurvey


# 11.1 测试函数
# 单元测试和测试用例
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('lennon', 'wang')
        self.assertEqual(formatted_name, 'Lennon Wang')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()


# 11.2 测试类
class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        # question = "What language did you first learn to speak? "
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response("English")
        # self.assertIn("English", my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        # for response in responses:
        #     my_survey.store_response(response)
        #
        # for response in responses:
        #     self.assertIn(response, my_survey.responses)
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()


