from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html', name="NIeznajomy\/nieznajmona")


@app.route("/<name>")
def hello_name(name):
    return render_template('main.html', name=name)

@app.route("/add_user", methods=['POST'])
def add_user():
    return f"Zaraz dodam user-a {request.form['username']}"


if __name__ == "__main__":
    app.run()


