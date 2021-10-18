import typing
import requests
import json

def func_1(name_currency:typing.Optional[str]) -> typing.Optional[float]:
    """Get three-digit alphabetic currency(str) code and return BYN currency rate(float)"""
    url = f'https://www.nbrb.by/api/exrates/rates/{name_currency}'
    params = {
        'parammode':2,
        'periodicity':0,
    }
    response = None
    try:
        response = requests.get(url=url, params=params)
        print(response.status_code)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

    # print(data['Cur_OfficialRate'])
    # print(data)
    data = response.json()
    if data['Cur_OfficialRate'] is not None:
        return round(data['Cur_OfficialRate'], 2)
    else:
        raise

def func_2():
    pass


if __name__ == '__main__':
    # print(func_1('USD'))
    # print(func_1('RUB'))
    func_2()