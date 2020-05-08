from flask import Flask, render_template, make_response, request

app = Flask(__name__, template_folder="templates")

path_to_data = "static/data.txt"

available_fields_to_write = ["Name", "Email", "Message", "Field5", "Check1",
                             "Check2", "Check3", "List"]

current_number = 1


@app.route('/')
def hello_world():
    return render_template("formPOST.html")


@app.route('/', methods=["POST"])
def getInfo():
    global current_number
    with open(path_to_data, "a") as file:
        file.write("Data number " + str(current_number) + "\n")
        for name in available_fields_to_write:
            try:
                print(request.form.get(name))
                file.write(request.form.get(name).replace("\r\n", "\\n"))
            except TypeError:
                continue
            except AttributeError:
                print("here")
                continue
            except:
                print(name)
                file.write(" #$#DAMAGED DATA#$#\n")
                return make_response(
                    "Something went wrong writing your data. Please, try again",
                    200)
            file.write(" #&# ")
        file.write("\n")
        current_number += 1
    return make_response('Test worked!', 200)


if __name__ == '__main__':
    app.run()
