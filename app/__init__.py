from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint

# Create the app >>---------->
app = Flask(__name__)

# Home Page | Loading a static page
@app.get("/")
def home():
    return render_template("pages/home.jinja")

# About Page | Loading a static page

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

# Random Number Page | Passing a value into the template

@app.get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template("pages/random.jinja", number = randNum)

# Number Page |  Passing a route value into the template

@app.get("/number/<int:gerald>")
def analyseNumber(gerald):
    return render_template("pages/number.jinja", enteredItem = gerald)

# Form Page | Loading a static page with a form

@app.get("/form/")
def form():
    return render_template("pages/form.jinja")


@app.post("/processForm/")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"],
        robot = request.form["robot?"]
    )

# Error Page | Returning error page when target is missing
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")