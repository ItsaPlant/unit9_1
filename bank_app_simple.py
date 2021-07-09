import csv

raw_data=[{"table":"C","no":"130/C/NBP/2021","tradingDate":"2021-07-07","effectiveDate":"2021-07-08","rates":[{"currency":"dolar amerykański","code":"USD","bid":3.7961,"ask":3.8727},{"currency":"dolar australijski","code":"AUD","bid":2.8498,"ask":2.9074},{"currency":"dolar kanadyjski","code":"CAD","bid":3.0500,"ask":3.1116},{"currency":"euro","code":"EUR","bid":4.4812,"ask":4.5718},{"currency":"forint (Węgry)","code":"HUF","bid":0.012562,"ask":0.012816},{"currency":"frank szwajcarski","code":"CHF","bid":4.1050,"ask":4.1880},{"currency":"funt szterling","code":"GBP","bid":5.2416,"ask":5.3474},{"currency":"jen (Japonia)","code":"JPY","bid":0.034288,"ask":0.03498},{"currency":"korona czeska","code":"CZK","bid":0.1739,"ask":0.1775},{"currency":"korona duńska","code":"DKK","bid":0.6026,"ask":0.6148},{"currency":"korona norweska","code":"NOK","bid":0.4365,"ask":0.4453},{"currency":"korona szwedzka","code":"SEK","bid":0.4404,"ask":0.4492},{"currency":"SDR (MFW)","code":"XDR","bid":5.3913,"ask":5.5003}]}]

rates = raw_data[0]['rates']

with open("D:\PRYWATNE\JEZYKI\Python\unit9\unit9_1\bank_quest_simple.csv", '', newline='') as csvfile:
    tablewriter=csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    tablewriter.writerow(rates[0].keys())

    for i, currency in enumerate(rates):
        tablewriter.writerow(rates[i].values())