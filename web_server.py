from flask import Flask, request
from flask_restful import Api, Resource, reqparse

import json
import parse_text

'''
Python 2.7 Implementation 

Local server that converts images to text and text to Braille

To run in command line: 
python web_server.py

Endpoint url: http://localhost:5000/braille
'''

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('image_url', required=True)

class Braille_Translation(Resource):
	def get(self, braille_type):
		args = parser.parse_args()
		image_url = args['image_url']

		if image_url is None:
			return {'data': []}

		text = parse_text.image_to_text(image_url)
		output_type = '{0}.json'.format(braille_type)

		if output_type == 'dots.json':
			result = parse_text.braille_dots(text, output_type)
		elif output_type == 'image.json':
			result = parse_text.braille_image(text, output_type)

		return {'data': output}

api.add_resource(Braille_Translation, '/braille/<string:braille_type>')		

if __name__ == '__main__':
	app.run()