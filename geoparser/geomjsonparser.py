import json
from shapely.geometry import shape, Point

data = []
with open("../drone-feedback-master/sources/geojson/5_mile_airport.geojson", "r") as map:
	data.append(json.load(map))
with open("../drone-feedback-master/sources/geojson/us_military.geojson", "r") as map:
	data.append(json.load(map))
with open("../drone-feedback-master/sources/geojson/us_national_park.geojson", "r") as map:
	data.append(json.load(map))
	


def canfly(coordinate):
	coordinate = Point(coordinate)
	for map in data:
		for feature in map['features']:
			polygon = shape(feature['geometry'])
			if polygon.contains(coordinate):
				print "You are too close to %s to fly a drone" %feature['properties']['name']
				return False;
			
			
	print "You can fly"
	return True
