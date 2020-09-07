from flask import Flask, jsonify, request

app = Flask(__name__)


stores= [
	{
		'name': 'My store',
		'items': [
			{
				'name': 'Item',
				'price': 2.80
			}
		]
	}
]


@app.route('/')
def index():
    return 'hello world!'


@app.route('/sotre', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
			'name': request_data['name']
			'items': []
		}
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass