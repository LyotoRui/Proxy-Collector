from posixpath import split
import requests
from templates import HEADER, AnonymityTypesTemplate, Proxy, ProxyTypesTemplate


def parse_proxyscrape(countries: list, types: list, anon: str) -> set[Proxy]:
    data = set()
    for country, type in zip(countries, types):
        response = requests.get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={type}&country={country}&anonymity={anon}', headers=HEADER).text
        for item in response.split('/n'):
            data.add(
                Proxy(
                    ip=item.split(':')[0],
                    port=item.split(':')[1],
                    type=type,
                    country=country
                )
            )
    return data

def get_from_proxyscrape(
    countries: list,
    types: list,
    anonimity: list,
) -> set[Proxy]:
    data = parse_proxyscrape(
        countries=countries,
        types=[ProxyTypesTemplate.PROXYSCRAPE.value.get(type) for type in types],
        anon=[AnonymityTypesTemplate.PROXYSCRAPE.value.get(type) for type in anonimity]
    )
    return data
