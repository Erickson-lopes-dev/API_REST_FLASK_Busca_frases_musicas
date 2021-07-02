from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Esta é a rota "/" by:<strong>Erickson Lopes da Silva</strong>'


@app.route('/name')
def index_name():
    return 'Meu nome é Erickson Lopes'


@app.route('/user/<username>')
def name(username):
    print(f'Olá usuário {escape(username)}')


if __name__ == '__main__':
    app.run(debug=True)
