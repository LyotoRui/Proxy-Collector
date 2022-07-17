import pytest
import requests

from parsers.hidemy import get_from_hidemy, parse_hidemy

def test_hidemy_connection():
    assert requests.get('https://hidemy.name/ru/proxy-list').status_code == 200
