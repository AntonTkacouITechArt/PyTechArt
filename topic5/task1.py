import typing
import  requests
import json
from bs4 import BeautifulSoup
import scrapy

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
    # url = 'https://yandex.by/pogoda/region/149'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    # }
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36',
    #
    # }
    # response = requests.get(url=url, headers=headers)
    #
    # print(response.text)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    # # print(soup.tag['class']='place-list__item-name')
    res = scrapy.fetch('https://yandex.by/pogoda/region/149')
    print(res)
    pass


if __name__ == '__main__':
    # print(func_1('USD'))
    # print(func_1('RUB'))
    func_2()