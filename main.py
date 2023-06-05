import pandas as pd
import requests
from http import HTTPStatus
from faker import Faker
from flask import Flask, Response, request


app = Flask(__name__)

@app.route('/students')
def students_generator():
    students_quantity =  int(request.args.get('quantity', '10'))
    if 1 <= students_quantity <= 1000:
        faker_instance = Faker('UK')
        person = {'first_name' : lambda: faker_instance.first_name(),
              'last_name': lambda: faker_instance.last_name(),
              'email': lambda: faker_instance.email(),
              'password': lambda: faker_instance.password(),
              'bithday': lambda: faker_instance.date_of_birth(minimum_age=18, maximum_age=60).strftime("%d-%m-%Y")}
        students = []
        for _ in range(students_quantity):
            students.append({key: generator() for key, generator in person.items()})
        df = pd.DataFrame(students)
        df.to_csv('students.csv', index=False)
        return df.to_html()
    else:
        return 'ERROR: should be a digit between 1 and 1000'

@app.route('/btc-rate')
def get_bitcoin_value():
    currency = request.args.get('currency', 'USD')
    amount_of_btc = int(request.args.get('amount', '100'))
    if amount_of_btc < 0:
        return 'ERROR: should be a digit more than 0'
    rates = pd.DataFrame(requests.get('https://bitpay.com/api/rates', {}).json())
    rate = rates.loc[rates['code'] == currency, 'rate'].values[0]
    converted_amount = amount_of_btc * rate
    symbols_list = requests.get('https://bitpay.com/currencies', {}).json()
    symbols_df = pd.DataFrame(symbols_list['data'], columns=['code', 'symbol'])
    symbol = symbols_df.loc[symbols_df['code'] == currency, 'symbol'].values[0]
    result = f'1 BTC = {rate} {symbol};\n{amount_of_btc} BTC = {converted_amount} {symbol}'
    return result




if __name__ == '__main__': app.run(port=5000, debug=False)