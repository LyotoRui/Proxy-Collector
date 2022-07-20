from black import main
from collector import Collector
from flask import Blueprint, jsonify, render_template, request
from models import Countries

main = Blueprint("index", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    match request.method:
        case "POST":
            request_data = request.get_json()["data"]
            response_data = Collector.do_work(
                countries=request_data["countries"] if len(request_data["countries"]) else ["US"],
                types=request_data["types"] if len(request_data["types"]) else ["HTTP"],
                anon=request_data["anon"] if len(request_data["anon"]) else ["HIGH"],
                format=request_data["format"] if len(request_data["format"]) == 1 else ["json"],
            )
            return jsonify(response_data)
        case "GET":
            return render_template(
                "index.html",
                countries=zip(
                    Countries.get_list_of_names(), Countries.get_list_of_values()
                ),
            )
