import requests
from bs4 import BeautifulSoup
from models import HEADER, AnonymityTypesTemplate, Proxy, ProxyTypesTemplate
from requests.exceptions import ReadTimeout


def parse_hidemy(limit: int, countries: list[str], type: str, anon: str) -> set | None:
    for country in countries:
        try:
            response = requests.get(
                f"https://hidemy.name/ru/proxy-list/?country={country}&type={type}&anon={anon}#list",
                headers=HEADER,
                timeout=5,
            ).text
        except ReadTimeout:
            return set()

        soup = BeautifulSoup(response, "lxml")

        table = soup.find(class_="table_block").find("tbody").find_all("tr")

        data = set()
        for index, row in zip(range(limit), table):
            try:
                line = row.find_all("td")
                data.add(
                    Proxy(
                        ip=line[0].text.strip(),
                        port=line[1].text.strip(),
                        type=line[4].text.strip(),
                        country=country,
                    )
                )
            except IndexError:
                return data
        return data


def get_from_hidemy(
    limit: int,
    countries: list,
    types: list,
    anonimity: list,
) -> set:
    data = parse_hidemy(
        limit=limit,
        countries=countries,
        type="".join([ProxyTypesTemplate.HIDEMY.value[type] for type in types]),
        anon="".join([AnonymityTypesTemplate.HIDEMY.value[type] for type in anonimity]),
    )
    return data
