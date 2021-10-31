import typing
from flask import Flask, render_template, redirect, request, make_response
from flask.json import jsonify
import requests
import json

app = Flask(__name__)


# CONSTANTS
URLHTTMLDICT = {
    '/': 'index.html',
    '/change/': 'index_change.html',
}


@app.before_first_request
def get_data_currency():
    """Get data currency from api nbrb"""
    with open('currency.json', 'w') as json_file:
        json_file.write(requests.get(
            'https://www.nbrb.by/api/exrates/currencies/').text)


@app.route('/', methods=['GET', 'POST'])
@app.route('/change/', methods=['GET', 'POST'])
def exchange_currency():
    """Main function of sites"""
    with open('currency.json', 'r') as json_file:
        data_currency = json.load(json_file)
    data = {
        'currency': [cur['Cur_Abbreviation'] for cur in data_currency],
        'cur_val_1': 0,
        'cur_val_2': 0,
    }
    if request.method == 'GET':
        return render_template(URLHTTMLDICT.get(request.path), data=data)
    elif request.method == 'POST':
        data = request.get_json()
        if request.path == '/':
            data['cur_val_2'] = round(
                [
                    byn_exchange(data['currency_2'], float(data['cur_val_1']))
                    for cur in data_currency
                    if data['currency_2'] == cur['Cur_Abbreviation']
                ][0], 2)
        elif request.path == '/change/':
            data['cur_val_2'] = round(
                [
                    foreign_exchange(data['currency_1'],
                                     float(data['cur_val_1']))
                    for cur in data_currency
                    if data['currency_1'] == cur['Cur_Abbreviation']
                ][0], 2)
        return make_response(jsonify(data))


def foreign_exchange(currency_name: typing.Optional[str],
                     currency_value: typing.Optional[float]) -> float:
    """Exchange foreign currency to BYN"""
    response = get_json_currency(currency_name)
    return currency_value * float(response['Cur_OfficialRate']) / float(
        response['Cur_Scale'])


def byn_exchange(currency_name: typing.Optional[str],
                 currency_value: typing.Optional[float]) -> float:
    """Exchange BYN currency to foreign currency"""
    response = get_json_currency(currency_name)
    return currency_value * float(response['Cur_Scale']) / float(
        response['Cur_OfficialRate'])


def get_json_currency(currency_name: typing.Optional[str]):
    """Get data about currency"""
    return requests.get(
        url=f"""https://www.nbrb.by/api/exrates/rates/{currency_name}""",
        params={'parammode': 2, 'periodicity': 0}).json()


@app.route('/update/')
def update_currency():
    print('update currency')
    get_data_currency()
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(debug=True)
