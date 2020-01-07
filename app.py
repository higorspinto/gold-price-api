from flask import Flask

from service import get_gold_price

app = Flask(__name__)

@app.route('/')
def index():

    json = get_gold_price()
    return json