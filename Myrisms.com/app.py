from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/articles")
def articles():
    return render_template("articles/articles.html")

@app.route("/event")
def event():
    return render_template("event/event.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/kpop")
def kpop():
    return render_template("articles/kpop/kpop.html")

@app.route("/kpopsemore")
def kpopsemore():
    return render_template("articles/kpop/kpop-semore.html")

@app.route("/kpop-example-seemore1")
def kpopexamplesemore1():
    return render_template("articles/kpop/example-seemore1.html")

@app.route("/kpop-example-seemore2")
def kpopexamplesemore2():
    return render_template("articles/kpop/example-seemore2.html")

@app.route("/kpop-example-seemore3")
def kpopexamplesemore3():
    return render_template("articles/kpop/example-seemore3.html")

@app.route("/kpop-example-seemore4")
def kpopexamplesemore4():
    return render_template("articles/kpop/example-seemore4.html")



@app.route("/kdrama")
def kdrama():
    return render_template("articles/kdrama/kdrama.html")

@app.route("/kdramasemore")
def kdramasemore():
    return render_template("articles/kdrama/kdrama-semore.html")

@app.route("/kdrama-example-seemore1")
def kdramaexamplesemore1():
    return render_template("articles/kdrama/example-seemore1.html")

@app.route("/kdrama-example-seemore2")
def kdramaexamplesemore2():
    return render_template("articles/kdrama/example-seemore2.html")

@app.route("/kdrama-example-seemore3")
def kdramaexamplesemore3():
    return render_template("articles/kdrama/example-seemore3.html")

@app.route("/kdrama-example-seemore4")
def kdramaexamplesemore4():
    return render_template("articles/kdrama/example-seemore4.html")



@app.route("/kbeuty")
def kbeuty():
    return render_template("articles/kbeuty/kbeuty.html")

@app.route("/kbeutysemore")
def kbeutysemore():
    return render_template("articles/kbeuty/kbeuty-semore.html")


@app.route("/kbeuty-example-seemore1")
def kbeutyexamplesemore1():
    return render_template("articles/kbeuty/example-seemore1.html")


@app.route("/kbeuty-example-seemore2")
def kbeutyexamplesemore2():
    return render_template("articles/kbeuty/example-seemore2.html")


@app.route("/kbeuty-example-seemore3")
def kbeutyexamplesemore3():
    return render_template("articles/kbeuty/example-seemore3.html")


@app.route("/kbeuty-example-seemore4")
def kbeutyexamplesemore4():
    return render_template("articles/kbeuty/example-seemore4.html")



@app.route("/knews")
def knews():
    return render_template("articles/knews/knews.html")

@app.route("/knewssemore")
def knewssemore():
    return render_template("articles/knews/knews-semore.html")

@app.route("/knews-example-seemore1")
def knewsexamplesemore1():
    return render_template("articles/knews/example-seemore1.html")

@app.route("/knews-example-seemore2")
def knewsexamplesemore2():
    return render_template("articles/knews/example-seemore2.html")

@app.route("/knews-example-seemore3")
def knewsexamplesemore3():
    return render_template("articles/knews/example-seemore3.html")

@app.route("/knews-example-seemore4")
def knewsexamplesemore4():
    return render_template("articles/knews/example-seemore4.html")



@app.route("/kmart")
def kmart():
    return render_template("articles/kmart/kmart.html")

@app.route("/kmartsemore")
def kmartsemore():
    return render_template("articles/kmart/kmart-semore.html")

@app.route("/kmart-example-seemore1")
def kmartexamplesemore1():
    return render_template("articles/kmart/example-seemore1.html")

@app.route("/kmart-example-seemore2")
def kmartexamplesemore2():
    return render_template("articles/kmart/example-seemore2.html")

@app.route("/kmart-example-seemore3")
def kmartexamplesemore3():
    return render_template("articles/kmart/example-seemore3.html")



@app.route("/kfood")
def kfood():
    return render_template("articles/kfood/kfood.html")

@app.route("/kfoodsemore")
def kfoodsemore():
    return render_template("articles/kfood/kfood-semore.html")

@app.route("/kfood-example-seemore1")
def kfoodexamplesemore1():
    return render_template("articles/kfood/example-seemore1.html")

@app.route("/kfood-example-seemore2")
def kfoodexamplesemore2():
    return render_template("articles/kfood/example-seemore2.html")

@app.route("/kfood-example-seemore3")
def kfoodexamplesemore3():
    return render_template("articles/kfood/example-seemore3.html")

@app.route("/kfood-example-seemore4")
def kfoodexamplesemore4():
    return render_template("articles/kfood/example-seemore4.html")




if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

