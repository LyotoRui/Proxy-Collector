import requests
from bs4 import BeautifulSoup
from models import HEADER, AnonymityTypesTemplate, Proxy, ProxyTypesTemplate
from requests.exceptions import ReadTimeout


def __parse_hidemy(limit: int, countries: list[str], type: str, anon: str) -> set | None:
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
    """
    Function that collects proxies from Hidemy.name.

    :param int limit: - Count of proxies from user`s input.
    :param list country: - List of coutries in Alpha-2.
    :param list type: - List of proxy types that required.
    :param list anon: - List of proxy anonymity types.
    :returns set[Proxy]: - Returns a set of Proxy objects
    """
    data = __parse_hidemy(
        limit=limit,
        countries=countries,
        type="".join([ProxyTypesTemplate.HIDEMY.value[type] for type in types]),
        anon="".join([AnonymityTypesTemplate.HIDEMY.value[type] for type in anonimity]),
    )
    return data
