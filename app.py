import csv
from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/currency/calc", methods=["GET", "POST"])
def calculator():
    if request.method=="GET":
        return render_template("calc.html")
    elif request.method=="POST":
        cur_1=request.form.get("cur_1")
        cur_2=request.form.get("cur_2")
