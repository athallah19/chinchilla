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
    return render_template("event.html")

@app.route("/admin")
def login():
    return render_template("login.html")



@app.route("/kpop")
def kpop():
    return render_template("articles/kpop.html")





if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

