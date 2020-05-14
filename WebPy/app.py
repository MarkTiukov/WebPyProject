from flask import Flask, render_template, make_response, request

app = Flask(__name__, template_folder="templates")

path_to_data = "static/data.txt"

available_fields_to_write = ["Name", "Email", "choice", "oval",
                             "heart", "oblong", "square", "round", "List"]

current_number = 1


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


@app.route('/')
def hello_world():
  return render_template("QuestioningExample.html")


@app.route('/', methods=["POST"])
def getInfo():
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
  return make_response('Test worked!', 200)


if __name__ == '__main__':
  app.run()
