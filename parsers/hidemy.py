import requests
from bs4 import BeautifulSoup

from templates import HEADER, ProxyTypesTemplate, AnonymityTypesTemplate

def parse_hidemy(limit: int, country: str, type: str, anon: str) -> set:
    response = requests.get(f'https://hidemy.name/ru/proxy-list/?country={country}&type={type}&anon={anon}#list', headers=HEADER).text

    soup = BeautifulSoup(response, 'lxml')

    table = soup.find(class_='table_block').find('tbody').find_all('tr')

    data = set()
    for index, row in zip(range(limit), table):
        try:
            line = row.find_all('td')
            ip = line[0].text.strip()
            port = line[1].text.strip()
            data.add(f'{ip}:{port}')
        except IndexError:
            return data
    return data


def get_from_hidemy(limit: int = 100, country: list = ['US'], types: list = ['HTTP'], anonimity: list = ['NONE']) -> set:
    data = parse_hidemy(
        limit=limit,
        country=''.join(country),
        type=''.join([ProxyTypesTemplate.HIDEMY.value[type] for type in types]),
        anon=''.join([AnonymityTypesTemplate.HIDEMY.value[type] for type in anonimity])
        )
    return data

