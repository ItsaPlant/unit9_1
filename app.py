import csv
from flask import Flask
from flask import request, redirect
from flask import render_template

data = {}
with open("bank_quest_simple.csv", newline='') as csvfile:
    csvreader = csv.reder(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        data[row[1]]=row[2]

app = Flask(__name__)

@app.route("/currency/calc", methods=["GET", "POST"])
def calculator():
    if request.method=="GET":
        return render_template("calc.html")
    elif request.method=="POST":
        cur_1=request.form.get("cur_1")
        quant=request.form.get('quant')

        #cur_1=data.get(cur_1)

        cost = cur_1 * quant

        return render_template("calc_result.html", cost=cost)
        

