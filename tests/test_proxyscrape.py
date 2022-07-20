import requests


def test_proxyscrape_connection():
    assert (
        requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies"
        ).status_code
        == 200
    )
