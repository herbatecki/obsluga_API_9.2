import requests

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()
print(data)
print(type(data))

import pickle

data_list = [
  {'currency': 'dolar amerykański', 'code': 'USD', 'bid': 3.7702, 'ask': 3.8464}, {'currency': 'dolar australijski', 'code': 'AUD', 'bid': 2.7876, 'ask': 2.844}, {'currency': 'dolar kanadyjski', 'code': 'CAD', 'bid': 2.9939, 'ask': 3.0543}, {'currency': 'euro', 'code': 'EUR', 'bid': 4.4699, 'ask': 4.5603},
  {'currency': 'forint (Węgry)', 'code': 'HUF', 'bid': 0.012824, 'ask': 0.013084},{'currency': 'frank szwajcarski', 'code': 'CHF', 'bid': 4.1154, 'ask': 4.1986}, {'currency': 'funt szterling', 'code': 'GBP', 'bid': 5.2022, 'ask': 5.3072}, {'currency': 'jen (Japonia)', 'code': 'JPY', 'bid': 0.034234, 'ask': 0.034926}, {'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.176, 'ask': 0.1796}, {'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.6011, 'ask': 0.6133}, {'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4354, 'ask': 0.4442}, {'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4403, 'ask': 0.4491}, {'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 5.3836, 'ask': 5.4924}
]

with open('/home/kacki/Documents/kodilla/virtual_flask/tasks/modul_9/9.2_obsluga_API/todo.pickle', 'wb') as f:
  pickle.dump(data_list, f)

with open('/home/kacki/Documents/kodilla/virtual_flask/tasks/modul_9/9.2_obsluga_API/todo.pickle', 'rb') as f:
  data_list = pickle.load(f)
print(data_list)
print(type(data_list))

import csv

with open('/home/kacki/Documents/kodilla/virtual_flask/tasks/modul_9/9.2_obsluga_API/currency_list.csv', mode='w') as currency_list:
  fieldnames = ['currency','code','bid','ask']
  currency_writer = csv.DictWriter(currency_list,fieldnames=fieldnames, delimiter = ";",quotechar ='"')

  currency_writer.writeheader()
  currency_writer.writerow({'currency': 'dolar amerykański', 'code': 'USD', 'bid': 3.7702, 'ask': 3.8464})
  currency_writer.writerow({'currency': 'dolar australijski', 'code': 'AUD', 'bid': 2.7876, 'ask': 2.844})
  currency_writer.writerow({'currency': 'euro', 'code': 'EUR', 'bid': 4.4699, 'ask': 4.5603})
  currency_writer.writerow({'currency': 'forint (Węgry)', 'code': 'HUF', 'bid': 0.012824, 'ask': 0.013084})
  currency_writer.writerow({'currency': 'frank szwajcarski', 'code': 'CHF', 'bid': 4.1154, 'ask': 4.1986})
  currency_writer.writerow({'currency': 'funt szterling', 'code': 'GBP', 'bid': 5.2022, 'ask': 5.3072})
  currency_writer.writerow({'currency': 'jen (Japonia)', 'code': 'JPY', 'bid': 0.034234, 'ask': 0.034926})
  currency_writer.writerow({'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.176, 'ask': 0.1796})
  currency_writer.writerow({'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.6011, 'ask': 0.6133})
  currency_writer.writerow({'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4354, 'ask': 0.4442})
  currency_writer.writerow({'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4403, 'ask': 0.4491})
  currency_writer.writerow({'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 5.3836, 'ask': 5.4924})


import pandas as pd
df = pd.read_csv('/home/kacki/Documents/kodilla/virtual_flask/tasks/modul_9/9.2_obsluga_API/currency_list.csv', delimiter=';')
print(df)
print(type(df))
print(df)
print(type(df))
print(df['code'])
eur = df[df.code=='EUR']['ask']
print(eur)

choice = 'USD'
res= df[df.code == choice]['ask']
print(res)
test = list(res)
print(test[0])

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def calculating_currencies():
    if request.method == 'POST':
        currency_data= request.form
        currency_choice = currency_data.get('value')
        amount_choice = currency_data.get('amount')
        compar = df[df.code == currency_choice]['ask']
        value = list(compar)
        element = value[0]
        return element*amount_choice
      
    return render_template('calculator.html')

if __name__=='__main__':
    app.run(debug=True)