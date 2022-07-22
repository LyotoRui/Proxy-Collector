import requests
from models import HEADER, AnonymityTypesTemplate, Proxy, ProxyTypesTemplate
from requests.exceptions import ReadTimeout


def __parse_geonode(limit: int, country: list, type: str, anon: str) -> set[Proxy]:
    data = set()
    for country in country:
        try:
            response = requests.get(
                f"https://proxylist.geonode.com/api/proxy-list?limit={limit}&page=1&country={country}&protocols={type}&{anon}",
                headers=HEADER,
                timeout=5,
            ).json()
        except ReadTimeout:
            return data
        proxies = response["data"]
        for item in proxies:
            data.add(
                Proxy(
                    ip=item["ip"],
                    port=item["port"],
                    type=item["protocols"][0],
                    country=country,
                )
            )
    return data


def get_from_geonode(
    limit: int,
    country: list,
    types: list,
    anonimity: list,
) -> set[Proxy]:
    """
    Function that collects proxies from Geonode.com.

    :param int limit: - Count of proxies from user`s input.

    :param list country: - List of coutries in Alpha-2.

    :param list type: - List of proxy types that required.

    :param list anon: - List of proxy anonymity types.
    """
    data = __parse_geonode(
        limit=limit,
        country=country,
        type="%2C".join([ProxyTypesTemplate.GEONODE.value[type] for type in types]),
        anon="&".join(
            [
                f"anonymityLevel={AnonymityTypesTemplate.GEONODE.value[type]}"
                for type in anonimity
            ]
        ),
    )
    return data
