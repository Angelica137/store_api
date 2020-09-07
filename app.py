from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'


@app.route('/sotre', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.rotue('/store/<string:name>/item')
def get_items_in_store(name):
    pass