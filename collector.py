from operator import attrgetter

from parsers.geonode import get_from_geonode
from parsers.hidemy import get_from_hidemy
from parsers.proxyscrape import get_from_proxyscrape
from models import Proxy
from tools import check_proxies, check_income_args, response_data_transformation
from exceptions import ArgsValidationError

class Collector:
    '''
    Base class to scrap proxy from different sources.
    '''
    @staticmethod
    def do_work(limit: int = 20, countries: list[str] = ['US'], types: list[str] = ['HTTP'], anon: list[str] = ['HIGH'], format: list[str] = ['json']) -> set[Proxy]:
        '''
        The only method in class.

        :params:

        limit - How many items should be returned.
        
        countries - In what country proxies shold be located. Countries must be as Alpha-2 code or use Country class from templates.

        types - What types this proxies should be. Use string params or use ProxyTypes class from templates.

        anon - Anonymity types. Use string params or use AnonymityTypes class from templates.
        '''
        if not check_income_args(
            countries=countries,
            types=types,
            anon=anon
        ):
            raise ArgsValidationError
        complite_data = set()
        geonode_data = get_from_geonode(
            limit=limit, country=countries, types=types, anonimity=anon
        )
        hidemy_data = get_from_hidemy(
            limit=limit, countries=countries, types=types, anonimity=anon
        )
        proxyscrape_data = get_from_proxyscrape(
            countries=countries, types=types, anonimity=anon
        )
        complite_data.update(geonode_data)
        complite_data.update(hidemy_data)
        complite_data.update(proxyscrape_data)
        checked_data = check_proxies(complite_data)
        print(checked_data)
        return response_data_transformation(format=format[0], data=checked_data, countries=countries)
