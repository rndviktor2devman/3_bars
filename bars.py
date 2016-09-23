import json
import math


def load_data(filepath):
    with open(filepath) as data_file:
    	data = json.loads(data_file.read())
    return data


def get_biggest_bar(data):
    biggest = data[0]
    for bar in data:
    	if bar['Cells']['SeatsCount'] >= biggest['Cells']['SeatsCount']:
    		biggest = bar

    return biggest


def get_smallest_bar(data):
    smallest = data[0]
    for bar in data:
    	if bar['Cells']['SeatsCount'] <= smallest['Cells']['SeatsCount']:
    		smallest = bar

    return smallest


def get_closest_bar(data, longitude, latitude):
	closest_bar = data[0]
	longitude_b = closest_bar['Cells']['geoData']['coordinates'][0]
	latitude_b = closest_bar['Cells']['geoData']['coordinates'][1]
	closest_range = math.sqrt(math.pow((longitude - longitude_b),2) + math.pow((latitude - latitude_b),2))
	for bar in data:
		longitude_b = bar['Cells']['geoData']['coordinates'][0]
		latitude_b = bar['Cells']['geoData']['coordinates'][1]
		check_range = math.sqrt(math.pow((longitude - longitude_b),2) + math.pow((latitude - latitude_b),2))
		if check_range <= closest_range:
			closest_range = check_range
			closest_bar = bar

	return closest_bar


if __name__ == '__main__':
    data = load_data('Bars.json')
    print('biggest:', get_biggest_bar(data))
    print('smallest:', get_smallest_bar(data))
    longitude = float(input('Please, enter longitude:'))
    latitude = float(input('Please, enter latitude:'))
    print('closest:', get_closest_bar(data, longitude, latitude))

