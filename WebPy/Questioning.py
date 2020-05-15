class Questioning:
  def __init__(self):
    self.questions = list()
    self.fields_to_write = set()
    self.addQuestions()

  def getNumber(self):
    try:
      return int(input())
    except:
      print("<Bad input. Try again>")
      return self.getNumber()

  def addQuestions(self):
    print("<Type number of questions in your questioning> ")
    number_of_questions = self.getNumber()
    for i in range(number_of_questions):
      current_question = dict()
      print("<Type the question> ")
      current_question["question"] = input()
      print("<Type its type (check or radio)> ")
      current_question["type"] = input()
      print("<Type number of answers> ")
      answers = list()
      for j in range(self.getNumber()):
        print("<Enter detailed answer> ")
        first = input()
        print("<Enter short answer to be written in data file> ")
        second = input()
        self.fields_to_write.add(second)
        answers.append([first, second])
      current_question["answers"] = answers
      self.questions.append(current_question)
