from string import ascii_letters


def gotBadInput():
  print("<ERROR: Bad input. Try again>")


class Questioning:
  def __init__(self, number: int):
    self.questions = list()
    self.fields_to_write = set()
    self.number = number
    self.name = "DefaultName" + str(number)
    print("<Enter the name of your questioning>")
    self.name = self.getName()
    self.link = self.name.replace(" ", "")
    self.addQuestions()


  def getNumber(self):
    try:
      return int(input())
    except:
      gotBadInput()
      return self.getNumber()

  def getName(self):
    print("<Your name should contain only english letters and spaces>")
    print(
      "<You can enter '$' to skip this part, a default name would be given>")
    given = input()
    if given == "$":
      return self.name
    for letter in given:
      if not (letter in ascii_letters or letter == " "):
        gotBadInput()
        return self.getName()
    return given

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
