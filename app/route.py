from app import app
from flask import render_template
from app import start

@app.route("/")
def hello():

    "ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!"
    return render_template("index.html")


@app.route('/bot/<question>', methods=['POST'])
def post_javascript_data(question):
    response = start.ask_something(question)
    return response