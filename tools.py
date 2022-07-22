from time import monotonic

import requests
from loguru import logger

from models import HEADER, AnonymityTypes, Countries, Proxy, ProxyTypes


def response_data_transformation(
    format: str, data: set[Proxy], countries: list[str]
) -> str | dict:
    '''Function that transform data from set[Proxy] to text format.
    
    :param str format: - Format param. It could be TXT or JSON.
    :param set[Proxy] data: - Set of Proxy objects.
    :param list[str] countries: - List of Alpha-2 country codes from user input.
    :returns str | dict:  - Returns a string or a dict depending to format that user needed.
    '''
    match format:
        case "json":
            return __transform_data_to_json(data=data, countries=countries)
        case "txt":
            return __transform_data_to_txt(data=data)


def __transform_data_to_json(data: set[Proxy], countries: list[str]) -> dict:
    '''Function that transform data from set[Proxy] to JSON format.

    :param set[Proxy] data: - Set of Proxy objects.

    :param list[str] countries: - List of Alpha-2 country codes from user input.

    :returns dict: - Returns a dict, where keys are countries from user input and value is a list of proxies
    ''' 
    return {
        country: [proxy.to_json() for proxy in data if proxy.country == country]
        for country in countries
    }


def __transform_data_to_txt(data: set[Proxy]) -> str:
    '''Function that transform data from set[Proxy] to TXT format.

    :param set[Proxy] data: - Set of Proxy objects.

    :returns string: - Returns a string where every proxy separated by newline.
    ''' 
    return "\n".join(
        [f"{proxy.country}--{proxy.type}--{proxy.ip}:{proxy.port}" for proxy in data]
    )


def check_proxies(proxies: set[Proxy]) -> set[Proxy]:
    checked_proxies = set()
    for proxy in proxies:
        try:
            start = monotonic()
            requests.get(
                "https://infoport.pro",
                headers=HEADER,
                proxies={f"{proxy.type}": f"{proxy.type}://{proxy.ip}:{proxy.port}"},
                timeout=1,
            )
            proxy.speed = (monotonic() - start).__round__(2)
            checked_proxies.add(proxy)
        except Exception:
            continue
    return checked_proxies


def __check_country_arg(countries: list[str] | None = None) -> bool:
    match countries:
        case list():
            pass
        case _:
            return False
    for country in countries:
        if country.upper() not in Countries.get_list_of_values():
            return False
    return True


def __check_type_arg(types: list[str] | None = None) -> bool:
    match types:
        case list():
            pass
        case _:
            return False
    for type in types:
        if type.upper() not in ProxyTypes.get_list_of_values():
            return False
    return True


def __check_anon_arg(anon: list[str] | None = None) -> bool:
    match anon:
        case list() | None:
            pass
        case _:
            return False
    for type in anon:
        if type.upper() not in AnonymityTypes.get_list_of_values():
            return False
    return True


def check_income_args(
    countries: list[str] | None = None,
    types: list[str] | None = None,
    anon: list[str] | None = None,
) -> bool:
    return all(
        (
            __check_country_arg(countries=countries),
            __check_type_arg(types=types),
            __check_anon_arg(anon=anon),
        )
    )
