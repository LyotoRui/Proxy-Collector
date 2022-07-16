from bs4 import BeautifulSoup
import requests
from templates import HEADER, ProxyTypesTemplate, AnonymityTypesTemplate

def parse_geonode(limit: int, country: list, type: str, anon: str) -> set:
    data = set()
    for country in country:
        response = requests.get(
            f'https://proxylist.geonode.com/api/proxy-list?limit={limit}&page=1&country={country}&protocols={type}&{anon}',
            headers=HEADER
        ).json()
        proxies = response['data']
        for item in proxies:
            ip = item['ip']
            port = item['port']
            data.add(f'{ip}:{port}')
    return data


def get_from_geonode(limit: int = 1, country: list = ['US'], types: list = ['HTTP'], anonimity: list = ['NONE']) -> set:
    data = parse_geonode(
        limit=limit,
        country=country,
        type='%2C'.join([ProxyTypesTemplate.GEONODE.value[type] for type in types]),
        anon='&'.join([f'anonymityLevel={AnonymityTypesTemplate.GEONODE.value[type]}' for type in anonimity])
    )
    return data
