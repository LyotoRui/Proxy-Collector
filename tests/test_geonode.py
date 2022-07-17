import pytest
import requests

from parsers.geonode import parse_geonode, get_from_geonode


def test_geonode_connection():
    assert requests.get("https://proxylist.geonode.com/").status_code == 200


def test_geonode_api_response():
    response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=1").json()
    assert isinstance(response['data'], list)
    assert isinstance(response['data'][0], dict)
    assert isinstance(response['data'][0]['ip'], str)
    assert isinstance(response['data'][0]['anonymityLevel'], str)
    assert isinstance(response['data'][0]['country'], str)
    assert isinstance(response['data'][0]['port'], str)
    assert isinstance(response['data'][0]['protocols'], list)



    