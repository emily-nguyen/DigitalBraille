from flask import Flask, request
from flask_cors import CORS

import json
import parse_text

'''
Python 2.7 Implementation 

Local server that converts images to text and text to Braille

To run in command line: 
python web_server.py

Endpoint url: 
http://localhost:5000/braille/dots?image_url=<url of image>
http://localhost:5000/braille/image?image_url<url of image>
'''

app = Flask(__name__)
CORS(app)

# @app.route('/braille/dots')
# def get_braille_dots():
# 	output = {}
# 	output['data'] = []
# 	image_url = request.args.get('image_url', None)

# 	if image_url is None:
# 		return json.dumps(output)

# 	text = parse_text.image_to_text(image_url)
# 	result = parse_text.braille_dots(text)

# 	if result is None:
# 		return json.dumps(output)

# 	output['data'] = result

# 	# with open('dots.json', 'w') as f:
# 	# 	json.dump(output, f)	

# 	return json.dumps(output)

@app.route('/braille/dots')
def get_braille_dots():
	with open('dots.json', 'r') as f:
		dots = json.load(f)

		return json.dumps(dots)

@app.route('/braille/image')
def get_braille_image():
	with open('image.json', 'r') as f:
		image = json.load(f)
		
		return json.dumps(image)

# @app.route('/braille/image')
# def get_braille_image():
# 	output = {}
# 	output['data'] = []
# 	input_text = request.args.get('input_text', None)

# 	if input_text is None:
# 		return json.dumps(output)

# 	text = parse_text.image_to_text(input_text)
# 	result = parse_text.braille_image(text)

# 	if result is None:
# 		return json.dumps(output)

# 	output['data'] = result

# 	# with open('image.json', 'w') as f:
# 	# 	json.dump(output, f)	

# 	return json.dumps(output)

if __name__ == '__main__':
	app.run()