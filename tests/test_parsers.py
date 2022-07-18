import random
from parsers.geonode import parse_geonode
from parsers.hidemy import parse_hidemy
from parsers.proxyscrape import parse_proxyscrape
from templates import Proxy, Countries, ProxyTypesTemplate, AnonymityTypesTemplate



def test_geonode_parser():
    data = parse_geonode(
        random.choice(range(1, 20)),
        random.choice(Countries.get_list_of_values()),
        random.choice(list(ProxyTypesTemplate.GEONODE.value.values())),
        random.choice(list(AnonymityTypesTemplate.GEONODE.value.values()))
    )
    assert isinstance(data, set)
    for item in data:
        assert isinstance(item, Proxy)

def test_hidemy_parser():
    data = parse_hidemy(
        random.choice(range(1, 20)),
        random.choice(Countries.get_list_of_values()),
        random.choice(list(ProxyTypesTemplate.HIDEMY.value.values())),
        random.choice(list(AnonymityTypesTemplate.HIDEMY.value.values()))
    )
    assert isinstance(data, set)
    for item in data:
        assert isinstance(item, Proxy)


def test_proxyscrape_parser():
    data = parse_proxyscrape(
        random.choice(Countries.get_list_of_values()),
        random.choice(list(ProxyTypesTemplate.HIDEMY.value.values())),
        random.choice(list(AnonymityTypesTemplate.HIDEMY.value.values()))
    )
    assert isinstance(data, set)
    for item in data:
        assert isinstance(item, Proxy)