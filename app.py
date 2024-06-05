from flask import Flask, render_template, request

app = Flask(__name__)

class car:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

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

@app.route("/obj")
def obj():
    cars = car("Tesla", "Audi", "BMW")
    return render_template("obj.html", car = cars)

@app.route("/conditional")
def condtional():
    company = "Apple"
    return render_template("conditional.html", company = company)

@app.route("/subscription", methods = ['GET', 'POST'])
def subscription():
    if request.method == "POST":
        mail = request.form.get("email")
        print(mail)
    return render_template("subscription_form.html")