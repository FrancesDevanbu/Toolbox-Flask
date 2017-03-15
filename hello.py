from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello World


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if not name:
        return 'index page'
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
