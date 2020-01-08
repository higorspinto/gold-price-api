from flask import Flask

from service import get_gold_price

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    json = get_gold_price()
    return json

if __name__ == '__main__':
    app.run(threaded=True, port=5000)