from flask import Flask, render_template, make_response, request, redirect
import threading
import logging

from Questioning import Questioning

app = Flask(__name__, template_folder="templates")

path_to_data = "static/data.txt"

available_fields_to_write = ["Name", "Email", "choice", "oval",
                             "heart", "oblong", "square", "round", "List"]

questionings = list()

current_number = 1


@app.route("/", methods=["GET"])
def mainPage():
  return render_template("mainPage.html", questionings=questionings)


def findCurrentQuestioning(questioning_id):
  result = None
  for questioning in questionings:
    if questioning.link == questioning_id:
      result = questioning
      break
  return result


@app.route("/answer/<questioning_id>", methods=["GET"])
def showQuestioning(questioning_id=None):
  questioning = findCurrentQuestioning(questioning_id)
  if questioning is not None:
    return render_template("formTemplate.html",
                           questions=questioning.questions)
  return make_response("Something went wrong", 404)


@app.route('/answer/<questioning_id>', methods=["POST"])
def getInfo(questioning_id=None):
  current_question = findCurrentQuestioning(questioning_id)
  global current_number
  with open(path_to_data, "a") as file:
    file.write("Data number " + str(
      current_number) + " for Questioning '" + current_question.name + "'\n")
    print("fields: ", current_question.fields_to_write)
    for name in current_question.fields_to_write:
      try:
        print("got", request.form.get(name))
        request.form.get(name)
        file.write(name)
        file.write("=")
        file.write(request.form.get(name))
      except TypeError:
        print("<type error>")
        continue
      except AttributeError:
        print("<attribute error>")
        continue
      except:
        print(name)
        file.write(" $$#DAMAGED DATA#$$\n")
        return make_response(
          "Something went wrong writing your data. Please, try again",
          200)
      file.write("&&")
    file.write("\n")
    current_number += 1
  return redirect("/")


def createNewQuestioning():
  questionings.append(Questioning(len(questionings) + 1))


def secondThread():
  print("<Enter 'make' to create a new questioning>")
  while True:
    command = input()
    if command == "make":
      createNewQuestioning()
    else:
      print("<Error: unknown command. Try again>")
  logging.info("THREAD 2 RUNNING")


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                    datefmt="%H:%M:%S")
second_thread = threading.Thread(target=secondThread, daemon=True)
second_thread.start()


@app.route("/testtemplateform")
def testTemplateForm():
  questions = [{"question": "Do you wear glasses?", "type": "radio",
                "answers": [["Of course I do", "Yes"],
                            ["No, I dont use them", "No"]]},
               {"question": "Do you need glasses?", "type": "radio",
                "answers": [["Unfortunately I do need them", "Yep"],
                            ["No, I dont need'em", "Nope"]]},
               {"question": "What glasses do you like?", "type": "check",
                "answers": [["I like oval glasses", "oval"],
                            ["I like heart shaped glasses", "heart"],
                            ["I like squared glasses", "square"]]},
               {"question": "What glasses do you can't stand?", "type": "check",
                "answers": [["I hate oval glasses", "oval"],
                            ["I hate heart shaped glasses", "heart"],
                            ["I hate squared glasses", "square"]]}]
  return render_template("formTemplate.html", questions=questions)


@app.route('/ExampleOfQuestioning')
def example():
  return render_template("QuestioningExample.html")


@app.route('/ExampleOfQuestioning', methods=["POST"])
def getInfoFromExample():
  global current_number
  with open(path_to_data, "a") as file:
    file.write("Data number " + str(current_number) + "\n")
    for name in available_fields_to_write:
      try:
        print("got", request.form.get(name))
        file.write(request.form.get(name).replace("\r\n", "\\n"))
      except TypeError:
        print("<type error>")
        continue
      except AttributeError:
        print("<attribute error>")
        continue
      except:
        print(name)
        file.write(" $$#DAMAGED DATA#$$\n")
        return make_response(
          "Something went wrong writing your data. Please, try again",
          200)
      file.write("&&")
    file.write("\n")
    current_number += 1
  return redirect("/")


##############################################################################

number_of_questions = 1


@app.route("/create_questioning", methods=["POST"])
def createQuestioningFromWeb():
  new_questioning = Questioning(len(questionings) + 1)
  new_questioning.setName(request.form["questioningName"])
  counter = 0
  print(request.form)
  while "question" + str(counter) in request.form:
    new_questioning.addQuestion(request.form, counter)
    counter += 1
  questionings.append(new_questioning)
  global number_of_questions
  number_of_questions = 1
  return redirect("/")


@app.route("/createmode", methods=["GET"])
def enterCreationMode():
  global number_of_questions
  return render_template("createQuestioning.html",
                         number_of_questions=number_of_questions)


@app.route("/add_question", methods=["POST"])
def addQuestion():
  global number_of_questions
  number_of_questions += 1
  return redirect("/createmode")


if __name__ == '__main__':
  app.run(port=2205)
