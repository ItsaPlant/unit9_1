import pickle
import requests
import json
import pickle
import csv

from werkzeug.datastructures import MultiDict

responce = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data_json = responce.json()
# print(type(data_json))
# print(data_json)

with open("todo.pickle", 'wb') as f:
    pickle.dump(data_json, f)

with open("todo.pickle", "rb") as f:
    data = pickle.load(f)

rates = data[0]['rates']
with open("bank_quest.csv", 'w', newline='') as csvfile:
    tablewriter=csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    tablewriter.writerow(rates[0].keys())

    for i, currrency in enumerate(rates):
        tablewriter.writerow(rates[i].values())
