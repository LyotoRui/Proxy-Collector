from time import monotonic

import requests
from loguru import logger

from templates import HEADER, Proxy


def check_proxies(proxies: set[Proxy]) -> set:
    checked_proxies = set()
    for proxy in proxies:
        try:
            start = monotonic()
            requests.get(
                "https://infoport.pro",
                headers=HEADER,
                proxies={"http": f"http://{proxy.ip}:{proxy.port}"},
                timeout=3,
            )
            proxy.speed = monotonic() - start
            checked_proxies.add(proxy)
        except Exception as error:
            continue
    return checked_proxies
