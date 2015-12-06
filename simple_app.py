from flask import Flask
from flask import render_template

# dunder: A quick way of saying "double underscore".
app = Flask(__name__)


# View: A view is a function that returns an HTTP response. This response has to be a string but can be any string you
# want.
# Route: A route is the URL path to a view. They always start with a forward slash / and can end with one if you want.

@app.route('/')
@app.route('/<name>')
def index(name='Treehouse'):
    return render_template("index.html", name=name)


@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
def multiply(num1=5, num2=5):
    return str(num1 * num2)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context)

app.run(debug=True, port=8000, host='0.0.0.0')
