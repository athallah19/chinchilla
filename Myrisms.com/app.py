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


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
