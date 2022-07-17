from operator import attrgetter

from parsers.geonode import get_from_geonode
from parsers.hidemy import get_from_hidemy
from templates import Proxy
from tools import check_proxies


class Collector:
    @staticmethod
    def do_work(limit: int, country: list, types: str, anon: str) -> set[Proxy]:
        complite_data = set()
        geonode_data = get_from_geonode(
            limit=limit, country=country, types=types, anonimity=anon
        )
        hidemy_data = get_from_hidemy(
            limit=limit, countries=country, types=types, anonimity=anon
        )
        complite_data.update(geonode_data)
        complite_data.update(hidemy_data)
        checked_data = check_proxies(complite_data)
        return sorted(checked_data, key=attrgetter("speed"))


print(Collector.do_work(limit=100, country=["US"], types=["HTTP"], anon=["HIGH"]))
