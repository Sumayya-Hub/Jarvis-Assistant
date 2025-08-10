from flask import Flask, render_template, request
from assistant import handle_command

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["command"]
        response = handle_command(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)