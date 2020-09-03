#!/usr/bin/python3
"""First flask app"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbn():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbn2():
    return 'HBNB'


@app.route('/c/<text>')
def hello_hbn3(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def hello_hbn4(text='is cool'):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>')
def hello_hbn5(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def hello_hbn6(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
