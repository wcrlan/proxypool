from flask import Flask, g, jsonify, request

from db import db

__all__ = ['app']

app = Flask(__name__)


@app.before_request
def get_conn():
    if not hasattr(g, 'db'):
        g.db = db


@app.route('/')
def index():
    return "<h1>Proxy Pool Stytem</h1><a href='/p'>get one proxy</a><p>or many by setting param-count<p>"


@app.route('/p')
def get():
    args = request.args
    count = args.get('count') if args.get('count') else 1
    return jsonify(g.db.get(count))


def api_process(port):
    print('api server start http://localhost:%s' % port)
    app.run(port=port)


if __name__ == '__main__':
    app.run(debug=True)
