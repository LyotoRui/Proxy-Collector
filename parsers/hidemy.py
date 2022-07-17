import requests
from bs4 import BeautifulSoup
from templates import HEADER, AnonymityTypesTemplate, Proxy, ProxyTypesTemplate


def parse_hidemy(limit: int, countries: str, type: str, anon: str) -> set:
    for country in countries:
        response = requests.get(
            f"https://hidemy.name/ru/proxy-list/?country={country}&type={type}&anon={anon}#list",
            headers=HEADER,
        ).text

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
                        country=country,
                    )
                )
            except IndexError:
                return data
        return data


def get_from_hidemy(
    limit: int = 100,
    countries: list = ["US"],
    types: list = ["HTTP"],
    anonimity: list = ["NONE"],
) -> set:
    data = parse_hidemy(
        limit=limit,
        countries=countries,
        type="".join([ProxyTypesTemplate.HIDEMY.value[type] for type in types]),
        anon="".join([AnonymityTypesTemplate.HIDEMY.value[type] for type in anonimity]),
    )
    return data
