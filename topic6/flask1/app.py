from flask import Flask, render_template
from markupsafe import escape
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    return render_template('index.html')


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
# @app.route('/<name>/', methods=['GET', ])
# def use_escape_for_unsecrity_data(name):
#     return f'<h1>Hello, {escape(name)}</h1>'
#
# @app.route('/index/')
# @app.route('/index/<string:name>',methods=['GET', ])
# def index_page(name=None):
#     return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
