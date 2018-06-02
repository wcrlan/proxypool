from flask import Flask, g, jsonify, request
import random
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
    count = int(args.get('count')) if args.get('count') else 1
    valid_list = g.db.get_valid()
    length = len(valid_list)
    if length == 0:
        return '<h1>代理池没有可用的代理</h1>'
    if count == 1:
        return random.choice(valid_list)
    if count > length:
        return '<h1>代理池数量不足</h1>'
    else:
        return jsonify(random.sample(valid_list, count))



if __name__ == '__main__':
    app.run(debug=True)
