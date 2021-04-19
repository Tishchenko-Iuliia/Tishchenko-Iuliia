import flask
from flask import Flask, request
from is_simple import is_simple

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return 'Just a plain text: "Hello from Flask!"' + (' With param ' + text if text else '')


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name')
def hello_name():
    name_param=request.args.getlist('name')
    name_list = list(map(int, name_param))

    if name_list == []:
        name_list = [0]

    a = name_list[0]
    answer = is_simple(a)

    return flask.render_template(
        'name.html',
        name=answer,
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)