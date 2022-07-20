import pytest
import requests


def test_hidemy_connection():
    assert requests.get("https://hidemy.name/ru/proxy-list").status_code == 200
