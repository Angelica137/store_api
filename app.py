from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'


@app.route('/sotre', methods=['POST'])
def create_store():
    pass


