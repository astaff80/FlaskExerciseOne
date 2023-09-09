
from operations import *

from flask import Flask

from flask import request

app = Flask(__name__)

@app.route('/<operation>')
def resolve(operation):
	a = request.args["a"]
	b = request.args["b"]
	val = f"{operation}({a},{b})"
	html = f"<html><body><h1>{eval(val)}</h1></body></html>"
	return html
