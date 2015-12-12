from flask import render_template
from app import app
import geomjsonparser as parser


def getShapes():
	maps = parser.getData()
	shapes = []
	for map in maps:
		for feature in map['features']:
			shapes.append(feature['geometry']['coordinates'][0])
			#print(feature['geometry'])
	#print shapes[0][0]
	#print "\n\n"
	#print shapes[1][0]
	return shapes
			

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/droneMap.html')
@app.route('/droneMap')
def dronemap():
	shapes = getShapes()
	return render_template('droneMap.html', shapes=shapes)
