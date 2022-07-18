from black import main
from flask import Blueprint, render_template, request

main = Blueprint('index', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    match request.method:
        case 'POST':
            pass
        case 'GET':
            return render_template('index.html')