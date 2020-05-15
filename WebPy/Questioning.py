from string import ascii_letters


def gotBadInput():
  print("<ERROR: Bad input. Try again>")


def success():
  print("<Created>")


class Questioning:
  def __init__(self, number: int):
    self.questions = list()
    self.fields_to_write = ["name", "email"]
    self.number = number
    self.name = "DefaultName" + str(number)
    # active in order to use console
    # print("<Enter the name of your questioning>")
    # self.name = self.getName()
    # self.link = self.name.replace(" ", "")
    # self.addQuestions()
    success()

  def setName(self, name):
    self.name = name
    if self.name is "DefaultName":
      self.name += str(self.number)
    self.link = self.name.replace(" ", "")

  def addQuestion(self, form_dict, number, answer_type="radio"):
    cur_question = dict()
    cur_question["question"] = form_dict["question" + str(number)]
    cur_question["type"] = answer_type
    self.fields_to_write.append("question" + str(number))
    cur_answers = list()
    for i in range(3):
      cur_answers.append([form_dict["answer" + str(number) + "_" + str(i)],
                          form_dict[
                            "short_answer" + str(number) + "_" + str(i)]])
    cur_question["answers"] = cur_answers
    self.questions.append(cur_question)

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
        print("#############TYPE", current_question["type"])
        if current_question["type"] == "check":
          print("here")
          self.fields_to_write.append("question" + str(i) + "_" + second)
        elif current_question["type"] == "radio" and "question" + \
                str(i) not in self.fields_to_write:
          self.fields_to_write.append("question" + str(i))
        answers.append([first, second])
      current_question["answers"] = answers
      self.questions.append(current_question)
