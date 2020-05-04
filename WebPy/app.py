from flask import Flask, render_template, make_response, request

app = Flask(__name__, template_folder="templates")

path_to_data = "static/data.txt"


@app.route('/')
def hello_world():
    return render_template("formPOST.html")


@app.route('/', methods=["POST"])
def getInfo():
    with open(path_to_data, "a") as file:
        file.write(request.form.get("Name"))
        file.write("\n")
    return make_response('Test worked!', 200)


if __name__ == '__main__':
    app.run()
