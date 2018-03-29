
from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
	# print(type(request.get_json()))
	res = request.get_json()
	if 'brands' in res:
		handle_res(res, 'inputs/brands.json')
	elif 'context' in res:
		handle_res(res, 'inputs/context.json')
	elif 'humans' in res:
		handle_res(res, 'inputs/humans.json')
	# print(res)
	# with open('out.json', 'a') as out:
	# 	out.write(json.dumps(res) + ',\n')
	# return 'Hello, World!'
	return 'nothing'


def handle_res(res, file):
	print(res)
	with open(file, 'a') as out:
		out.write(json.dumps(res) + ',\n')


