from flask import Flask, redirect, url_for, render_template, request, jsonify,session
from pymongo import MongoClient
import requests
import jwt
import hashlib
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from bson import ObjectId

app = Flask(__name__)

SECRET_KEY = "SPARTA"
TOKEN_KEY = 'mytoken'

client = MongoClient('mongodb://sparta:test@ac-ez4p5sg-shard-00-00.vhjwf8r.mongodb.net:27017,ac-ez4p5sg-shard-00-01.vhjwf8r.mongodb.net:27017,ac-ez4p5sg-shard-00-02.vhjwf8r.mongodb.net:27017/?ssl=true&replicaSet=atlas-qtflix-shard-0&authSource=admin&retryWrites=true&w=majority')  # Ganti URL sesuai dengan pengaturan MongoDB Anda
db = client.myrism
 # Ganti 'mydatabase' dengan nama database Anda


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/event")
def event():
    return render_template("event.html")



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/tambahdata-event")
def tambahdataevent():
    return render_template("tambahdata-event.html")



@app.route("/kpop")
def kpop():
    return render_template("kpop.html")



@app.route("/login", methods=["GET"])
def login():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.login.find_one({"username": payload.get("id")})
        return redirect(url_for("dashboard", user_info=user_info))
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        msg = request.args.get("msg")
        return render_template("login.html", msg=msg)


@app.route("/login_save", methods=["POST"])
def login_save():
    username_receive = request.form["username_login"]
    password_receive = request.form["password_login"]
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    result = db.login.find_one(
        {"username": username_receive, "password": password_receive}
    )
    if result:
        payload = {
            "id": username_receive,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 1),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"result": "success", "token": token})
    else:
        return jsonify(
            {
                "result": "fail",
                "msg": "Kami tidak dapat menemukan pengguna dengan kombinasi id/kata sandi tersebut",
            }
        )


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
