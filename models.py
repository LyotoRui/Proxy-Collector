from enum import Enum

HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75"
}


class Proxy:
    '''Base class for proxy object.'''
    ip: str
    port: str
    type: str
    country: str
    speed: float

    def __init__(self, ip: str, port: str, type: str, country: str, speed: float = None) -> None:
        self.ip = ip
        self.port = port
        self.country = country
        self.type = type.lower()
        self.speed = speed

    def __repr__(self) -> str:
        return f"{self.country} -- {self.type} - {self.ip}:{self.port} - {self.speed}"
    
    def to_json(self):
        return {
            'ip': self.ip,
            'port': self.port,
            'type': self.type
        }

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
    PROXYSCRAPE = {'HTTP': 'http', 'HTTPS': 'http', 'SOCKS4': 'socks4', 'SOCKS5': 'socks5'}


class AnonymityTypesTemplate(Enum):
    HIDEMY = {"HIGH": "4", "MEDIUM": "3", "LOW": "2", "NONE": "1"}
    GEONODE = {
        "HIGH": "elite",
        "MEDIUM": "anonymous",
        "LOW": "anonymous",
        "NONE": "transparent"
    }
    PROXYSCRAPE = {
        "HIGH": "elite",
        "MEDIUM": "anonymous",
        "LOW": "anonymous",
        "NONE": "transparent"
    }


class Countries(Enum):
    '''
    Class than contains Alpha-2 codes of different countries.
    
    Inherited from Enum.
    '''
    AFGHANISTAN = "AF"
    ALBANIA = "AL"
    ALGERIA = "DZ"
    AMERICAN_SAMOA = "AS"
    ANDORRA = "AD"
    ANGOLA = "AO"
    ANGUILLA = "AI"
    ANTARCTICA = "AQ"
    ANTIGUA_AND_BARBUDA = "AG"
    ARGENTINA = "AR"
    ARMENIA = "AM"
    ARUBA = "AW"
    AUSTRALIA = "AU"
    AUSTRIA = "AT"
    AZERBAIJAN = "AZ"
    BAHAMAS = "BS"
    BAHRAIN = "BH"
    BANGLADESH = "BD"
    BARBADOS = "BB"
    BELARUS = "BY"
    BELGIUM = "BE"
    BELIZE = "BZ"
    BENIN = "BJ"
    BERMUDA = "BM"
    BHUTAN = "BT"
    BOSNIA_AND_HERZEGOVINA = "BA"
    BOTSWANA = "BW"
    BOUVET_ISLAND = "BV"
    BRAZIL = "BR"
    BRUNEI_DARUSSALAM = "BN"
    BULGARIA = "BG"
    BURKINA_FASO = "BF"
    BURUNDI = "BI"
    CABO_VERDE = "CV"
    CAMBODIA = "KH"
    CAMEROON = "CM"
    CANADA = "CA"
    CAYMAN_ISLANDS = "KY"
    CHAD = "TD"
    CHILE = "CL"
    CHINA = "CN"
    CHRISTMAS_ISLAND = "CX"
    COLOMBIA = "CO"
    COSTA_RICA = "CR"
    CROATIA = "HR"
    CUBA = "CU"
    CURAÇAO = "CW"
    CYPRUS = "CY"
    CZECHIA = "CZ"
    DENMARK = "DK"
    DJIBOUTI = "DJ"
    DOMINICA = "DM"
    DOMINICAN_REPUBLIC = "DO"
    ECUADOR = "EC"
    EGYPT = "EG"
    EL_SALVADOR = "SV"
    EQUATORIAL_GUINEA = "GQ"
    ERITREA = "ER"
    ESTONIA = "EE"
    ESWATINI = "SZ"
    ETHIOPIA = "ET"
    FIJI = "FJ"
    FINLAND = "FI"
    FRANCE = "FR"
    FRENCH_GUIANA = "GF"
    FRENCH_POLYNESIA = "PF"
    GABON = "GA"
    GEORGIA = "GE"
    GERMANY = "DE"
    GHANA = "GH"
    GIBRALTAR = "GI"
    GREECE = "GR"
    GREENLAND = "GL"
    GRENADA = "GD"
    GUADELOUPE = "GP"
    GUAM = "GU"
    GUATEMALA = "GT"
    GUERNSEY = "GG"
    GUINEA = "GN"
    GUYANA = "GY"
    HAITI = "HT"
    HONDURAS = "HN"
    HONG_KONG = "HK"
    HUNGARY = "HU"
    ICELAND = "IS"
    INDIA = "IN"
    INDONESIA = "ID"
    IRAQ = "IQ"
    IRELAND = "IE"
    ISLE_OF_MAN = "IM"
    ISRAEL = "IL"
    ITALY = "IT"
    JAMAICA = "JM"
    JAPAN = "JP"
    JERSEY = "JE"
    JORDAN = "JO"
    KAZAKHSTAN = "KZ"
    KENYA = "KE"
    KIRIBATI = "KI"
    KOREA = "KR"
    KUWAIT = "KW"
    KYRGYZSTAN = "KG"
    LATVIA = "LV"
    LEBANON = "LB"
    LESOTHO = "LS"
    LIBERIA = "LR"
    LIBYA = "LY"
    LIECHTENSTEIN = "LI"
    LITHUANIA = "LT"
    LUXEMBOURG = "LU"
    MACAO = "MO"
    MADAGASCAR = "MG"
    MALAWI = "MW"
    MALAYSIA = "MY"
    MALDIVES = "MV"
    MALI = "ML"
    MALTA = "MT"
    MARTINIQUE = "MQ"
    MAURITANIA = "MR"
    MAURITIUS = "MU"
    MAYOTTE = "YT"
    MEXICO = "MX"
    MICRONESIA = "FM"
    MOLDOVA = "MD"
    MONACO = "MC"
    MONGOLIA = "MN"
    MONTENEGRO = "ME"
    MONTSERRAT = "MS"
    MOROCCO = "MA"
    MOZAMBIQUE = "MZ"
    MYANMAR = "MM"
    NAMIBIA = "NA"
    NAURU = "NR"
    NEPAL = "NP"
    NETHERLANDS = "NL"
    NEW_CALEDONIA = "NC"
    NEW_ZEALAND = "NZ"
    NICARAGUA = "NI"
    NIGERIA = "NG"
    NIUE = "NU"
    NORFOLK_ISLAND = "NF"
    NORWAY = "NO"
    OMAN = "OM"
    PAKISTAN = "PK"
    PALAU = "PW"
    PANAMA = "PA"
    PAPUA_NEW_GUINEA = "PG"
    PARAGUAY = "PY"
    PERU = "PE"
    PHILIPPINES = "PH"
    PITCAIRN = "PN"
    POLAND = "PL"
    PORTUGAL = "PT"
    PUERTO_RICO = "PR"
    QATAR = "QA"
    RÉUNION = "RE"
    ROMANIA = "RO"
    RUSSIAN_FEDERATION = "RU"
    RWANDA = "RW"
    SAINT_BARTHÉLEMY = "BL"
    SAINT_KITTS_AND_NEVIS = "KN"
    SAINT_LUCIA = "LC"
    SAINT_PIERRE = "PM"
    SAINT_VINCENT = "VC"
    SAMOA = "WS"
    SAN_MARINO = "SM"
    SAO_TOME_AND_PRINCIPE = "ST"
    SAUDI_ARABIA = "SA"
    SENEGAL = "SN"
    SERBIA = "RS"
    SEYCHELLES = "SC"
    SIERRA_LEONE = "SL"
    SINGAPORE = "SG"
    SLOVAKIA = "SK"
    SLOVENIA = "SI"
    SOLOMON_ISLANDS = "SB"
    SOMALIA = "SO"
    SOUTH_AFRICA = "ZA"
    SOUTH_GEORGIA = "GS"
    SOUTH_SUDAN = "SS"
    SPAIN = "ES"
    SRI_LANKA = "LK"
    SURINAME = "SR"
    SVALBARD_AND_JAN_MAYEN = "SJ"
    SWEDEN = "SE"
    SWITZERLAND = "CH"
    SYRIAN_ARAB_REPUBLIC = "SY"
    TAIWAN = "TW"
    TAJIKISTAN = "TJ"
    THAILAND = "TH"
    TOGO = "TG"
    TOKELAU = "TK"
    TONGA = "TO"
    TRINIDAD_AND_TOBAGO = "TT"
    TUNISIA = "TN"
    TURKEY = "TR"
    TURKMENISTAN = "TM"
    TUVALU = "TV"
    UGANDA = "UG"
    UKRAINE = "UA"
    UNITED_ARAB_EMIRATES = "AE"
    GREAT_BRITAIN = "GB"
    UNITED_STATES_OF_AMERICA = "US"
    URUGUAY = "UY"
    UZBEKISTAN = "UZ"
    VANUATU = "VU"
    VENEZUELA = "VE"
    VIET_NAM = "VN"
    VIRGIN_ISLANDS_BRITISH = "VG"
    VIRGIN_ISLANDS_US = "VI"
    WALLIS_AND_FUTUNA = "WF"
    WESTERN_SAHARA = "EH"
    YEMEN = "YE"
    ZAMBIA = "ZM"
    ZIMBABWE = "ZW"

    def get_list_of_values():
        return [item.value for item in Countries]
    
    def get_list_of_names():
        return [item.name.replace('_', ' ') for item in Countries]
