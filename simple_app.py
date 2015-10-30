from flask import Flask
from flask import request

# dunder: A quick way of saying "double underscore".
app = Flask(__name__)


# View: A view is a function that returns an HTTP response. This response has to be a string but can be any string you
# want.
# Route: A route is the URL path to a view. They always start with a forward slash / and can end with one if you want.

@app.route('/')
def index(name="kaygee"):
    name = request.args.get('name', name)
    return "Hello from {}".format(name)

app.run(debug=True, port=8000, host='0.0.0.0')
