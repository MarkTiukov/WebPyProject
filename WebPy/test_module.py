import unittest

import app


class MyTestCase(unittest.TestCase):

  # this one tests work of addQuestion() and createQuestioningFromWeb
  def test_changing_number_back(self):
    app.addQuestion()
    app.addQuestion()
    self.assertEqual(app.number_of_questions, 3)
    with app.app.test_request_context("/create_questioning",
                                      data={'questioningName': 'My Name',
                                            'question0': 'First Question',
                                            'answer0_0': 'First answer',
                                            'short_answer0_0': '1',
                                            'answer0_1': 'Second answer',
                                            'short_answer0_1': '2',
                                            'answer0_2': 'third answer',
                                            'short_answer0_2': '3'}):
      app.createQuestioningFromWeb()
      self.assertEqual(app.number_of_questions, 1)

  def test_setting_name_to_questioning(self):
    from Questioning import Questioning
    testing_questioning = Questioning(7)
    testing_questioning.setName("DefaultName")
    self.assertEqual(testing_questioning.name, "DefaultName7")
    testing_questioning.setName("My own name with spaces XD")
    self.assertEqual(testing_questioning.name, "My own name with spaces XD")
    self.assertEqual(testing_questioning.link, "MyownnamewithspacesXD")

  def test_adding_questions(self):
    from Questioning import Questioning
    testing_questioning = Questioning(1)
    testing_questioning.setName("DefaultName")
    form_data = {'questioningName': 'My Name',
                 'question0': 'First Question',
                 'answer0_0': 'First answer',
                 'short_answer0_0': '1',
                 'answer0_1': 'Second answer',
                 'short_answer0_1': '2',
                 'answer0_2': 'third answer',
                 'short_answer0_2': '3',
                 'question1': 'First Question',
                 'answer1_0': 'First answer',
                 'short_answer1_0': '1',
                 'answer1_1': 'Second answer',
                 'short_answer1_1': '2',
                 'answer1_2': 'third answer',
                 'short_answer1_2': '3'}
    testing_questioning.addQuestion(form_data, 0)
    self.assertEqual(len(testing_questioning.questions), 1)
    self.assertEqual(len(testing_questioning.questions[0]["answers"]), 3)
    #####
    testing_questioning.addQuestion(form_data, 1)
    self.assertEqual(len(testing_questioning.questions), 2)
    self.assertEqual(len(testing_questioning.questions[1]["answers"]), 3)

  if __name__ == '__main__':
    unittest.main()
