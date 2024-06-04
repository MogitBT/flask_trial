from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    color = "Red"
    animal_one = "Fox"
    animal_two = "Bear"
    orange_amount = 10
    apple_amount = 20
    donate_amount = 5
    first_name = "Mogit"
    last_name = "B T"

    kywords = {
        "color" : color,
        "animal_one" : animal_one,
        "animal_two" : animal_two,
        "orange_amount" : orange_amount,
        "apple_amount" : apple_amount,
        "donate_amount" : donate_amount,
        "first_name" : first_name,
        "last_name" : last_name
    }

    return render_template("home.html", **kywords)