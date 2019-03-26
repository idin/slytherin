from math import sin, cos, sqrt, atan2, radians
import geopy.distance
earth_radius = 6373  # km

def get_haversine_distance(latitude1, longitude1, latitude2, longitude2, unit = 'km'):
	lat1 = radians(latitude1)
	lon1 = radians(longitude1)
	lat2 = radians(latitude2)
	lon2 = radians(longitude2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = earth_radius * c

	if unit.lower() != 'km':
		distance *= 0.621371

	return distance

def get_vincenty_distance(latitude1, longitude1, latitude2, longitude2, unit = 'km'):
	coords_1 = (latitude1, longitude1)
	coords_2 = (latitude2, longitude2)
	distance = geopy.distance.vincenty(coords_1, coords_2).km

	if unit.lower() != 'km':
		distance *= 0.621371

	return distance

def get_distance(latitude1, longitude1, latitude2, longitude2, unit = 'km', method = 'vincenty'):
	if method.lower() == 'vincenty':
		return get_vincenty_distance(
			latitude1 = latitude1, longitude1 = longitude1,
			latitude2 = latitude2, longitude2 = longitude2,
			unit = unit
		)
	else:
		return get_haversine_distance(
			latitude1=latitude1, longitude1=longitude1,
			latitude2=latitude2, longitude2=longitude2,
			unit=unit
		)


