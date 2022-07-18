from time import monotonic

import requests
from loguru import logger

from models import HEADER, AnonymityTypes, Countries, Proxy, ProxyTypes


def check_proxies(proxies: set[Proxy]) -> set:
    checked_proxies = set()
    for proxy in proxies:
        try:
            start = monotonic()
            requests.get(
                "https://google.com",
                headers=HEADER,
                proxies={f"{proxy.type}": f"{proxy.type}://{proxy.ip}:{proxy.port}"},
                timeout=3,
            )
            proxy.speed = (monotonic() - start).__round__(2)
            checked_proxies.add(proxy)
        except Exception as error:
            logger.error(error)
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
        if type not in AnonymityTypes.get_list_of_values():
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
        __check_anon_arg(anon=anon)
        )
    )
