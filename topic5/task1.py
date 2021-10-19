import typing
import requests
import json

def func_1(name_currency:typing.Optional[str]) -> typing.Optional[float]:
    """Get three-digit alphabetic currency(str) code and return BYN currency rate(float)"""
    response = None
    url = f'https://www.nbrb.by/api/exrates/rates/{name_currency}'
    params = {
        'parammode':2,
        'periodicity':0,
    }
    try:
        response = requests.get(url=url, params=params)
        print('status:' + str(response.status_code))
        response.raise_for_status()
        data = response.json()
        if data['Cur_OfficialRate'] is not None:
            return round(float(data['Cur_Scale'])/float(data['Cur_OfficialRate']), 2)
        raise
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def func_2():
    pass


if __name__ == '__main__':
    print(func_1('USD'))
    print(func_1('RUB'))
