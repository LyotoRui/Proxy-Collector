from collector import Collector
from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api")

# Request example:
# https://{your_adress}/api/get?countries=UA,US&types=HTTP,HTTPS&anon=HIGH,LOW


@api.route("/get")
def main():
    countries = request.args.get("countries")
    types = request.args.get("types")
    anon = request.args.get("anon")
    response_data = Collector.do_work(
        countries=countries.split(",") if countries else ["US"],
        types=types.split(",") if types else ["HTTP"],
        anon=anon.split(",") if anon else ["HIGH"],
    )
    return jsonify(response_data)
