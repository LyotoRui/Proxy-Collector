from enum import Enum

HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75"
}


class Proxy:
    """Base class for proxy object."""

    ip: str
    port: str
    type: str
    country: str
    speed: float

    def __init__(
        self, ip: str, port: str, type: str, country: str, speed: float = None
    ) -> None:
        self.ip = ip
        self.port = port
        self.country = country
        self.type = type.lower()
        self.speed = speed

    def __repr__(self) -> str:
        return f"{self.country} -- {self.type} - {self.ip}:{self.port} - {self.speed}"

    def to_json(self):
        return {"ip": self.ip, "port": self.port, "type": self.type}

    def to_string(self):
        return f"{self.country}--{self.type}--{self.ip}:{self.port}--{self.speed}"


class ProxyTypes(Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    SOCKS4 = "SOCKS4"
    SOCKS5 = "SOCKS5"

    def get_list_of_values():
        return [type.value for type in ProxyTypes]

    def get_list_of_names():
        return [type.name for type in ProxyTypes]


class AnonymityTypes(Enum):
    HIGH = "HIGH"
    MENIUIM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"

    def get_list_of_values():
        return [type.value for type in AnonymityTypes]

    def get_list_of_names():
        return [type.name for type in AnonymityTypes]


class ProxyTypesTemplate(Enum):
    HIDEMY = {"HTTP": "h", "HTTPS": "s", "SOCKS4": "4", "SOCKS5": "5"}
    GEONODE = {"HTTP": "http", "HTTPS": "https", "SOCKS4": "socks4", "SOCKS5": "socks5"}
    PROXYSCRAPE = {
        "HTTP": "http",
        "HTTPS": "http",
        "SOCKS4": "socks4",
        "SOCKS5": "socks5",
    }


class AnonymityTypesTemplate(Enum):
    HIDEMY = {"HIGH": "4", "MEDIUM": "3", "LOW": "2", "NONE": "1"}
    GEONODE = {
        "HIGH": "elite",
        "MEDIUM": "anonymous",
        "LOW": "anonymous",
        "NONE": "transparent",
    }
    PROXYSCRAPE = {
        "HIGH": "elite",
        "MEDIUM": "anonymous",
        "LOW": "anonymous",
        "NONE": "transparent",
    }


class Countries(Enum):
    """
    Class than contains Alpha-2 codes of different countries.

    Inherited from Enum.
    """

    ARGENTINA = "AR"
    ARMENIA = "AM"
    AUSTRALIA = "AU"
    AZERBAIJAN = "AZ"
    BANGLADESH = "BD"
    BELARUS = "BY"
    BELIZE = "BZ"
    BRAZIL = "BR"
    BULGARIA = "BG"
    CAMBODIA = "KH"
    CANADA = "CA"
    CHILE = "CL"
    CHINA = "CN"
    COLOMBIA = "CO"
    CURACAO = "CW"
    CYPRUS = "CY"
    DOMINICAN_REPUBLIC = "DO"
    ECUADOR = "EC"
    EGYPT = "EG"
    FINLAND = "FI"
    FRANCE = "FR"
    GEORGIA = "GE"
    GERMANY = "DE"
    GUINEA = "GN"
    HONG_KONG = "HK"
    HUNGARY = "HU"
    INDIA = "IN"
    INDONESIA = "ID"
    IRELAND = "IE"
    JAPAN = "JP"
    KAZAKHSTAN = "KZ"
    KENYA = "KE"
    KOREA = "KR"
    LITHUANIA = "LT"
    NETHERLANDS = "NL"
    POLAND = "PL"
    ROMANIA = "RO"
    RUSSIAN_FEDERATION = "RU"
    SPAIN = "ES"
    SWITZERLAND = "CH"
    TAIWAN = "TW"
    TURKEY = "TR"
    UKRAINE = "UA"
    UNITED_ARAB_EMIRATES = "AE"
    GREAT_BRITAIN = "GB"
    UNITED_STATES_OF_AMERICA = "US"
    YEMEN = "YE"
    ZAMBIA = "ZM"
    ZIMBABWE = "ZW"

    def get_list_of_values():
        return [item.value for item in Countries]

    def get_list_of_names():
        return [item.name.replace("_", " ") for item in Countries]
