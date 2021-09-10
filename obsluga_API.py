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
        currency_choice = currency_data.get('currency')
        amount_choice = currency_data.get('amount')
        compar = df[df.code == currency_choice]['ask']
        value = list(compar)
        amount_value = int(amount_choice)
        print(type(value))
        print(value)
        element=float(value[0])
        print(element)
        print(amount_value)
        result = str(amount_value*element)
        return f'W celu zakupu {amount_choice} {currency_choice} przygotuj {result} PLN.'
      
    return render_template('calculator.html')

if __name__=='__main__':
   app.run(debug=True)