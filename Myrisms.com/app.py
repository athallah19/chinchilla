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



@app.route("/kdrama-example-seemore1")
def kdramaexamplesemore1():
    return render_template("articles/kdrama/example-seemore1.html")



@app.route("/kbeuty-example-seemore1")
def kbeutyexamplesemore1():
    return render_template("articles/kbeuty/example-seemore1.html")



@app.route("/knews-example-seemore1")
def knewsexamplesemore1():
    return render_template("articles/knews/example-seemore1.html")



@app.route("/kmart-example-seemore1")
def kmartexamplesemore1():
    return render_template("articles/kmart/example-seemore1.html")



@app.route("/kfood-example-seemore1")
def kfoodexamplesemore1():
    return render_template("articles/kfood/example-seemore1.html")




if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

