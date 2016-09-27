import json
import math
import sys


def load_data(filepath):
    with open(filepath) as data_file:
    	data = json.loads(data_file.read())
    return data

def get_seats_count(bar):
	return bar['Cells']['SeatsCount']


def get_biggest_bar(data):
    biggest = data[0]
    for bar in data:
    	if get_seats_count(bar) >= get_seats_count(biggest):
    		biggest = bar

    return biggest


def get_smallest_bar(data):
    smallest = data[0]
    for bar in data:
    	if get_seats_count(bar) <= get_seats_count(smallest):
    		smallest = bar

    return smallest

def get_range_to_coordinats(bar, longitude, latitude):
	longitude_bar = bar['Cells']['geoData']['coordinates'][0]
	latitude_bar = bar['Cells']['geoData']['coordinates'][1]
	return math.sqrt(math.pow((longitude - longitude_bar),2) + math.pow((latitude - latitude_bar),2))


def get_closest_bar(data, longitude, latitude):
	closest_bar = data[0]
	closest_range = get_range_to_coordinats(closest_bar, longitude, latitude)
	for bar in data:
		check_range = get_range_to_coordinats(bar, longitude, latitude)
		if check_range <= closest_range:
			closest_range = check_range
			closest_bar = bar

	return closest_bar


if __name__ == '__main__':
	input_parameter = sys.argv[1]
	if input_parameter.lower().endswith('.json'):
		data = load_data(input_parameter)
		print('biggest:', get_biggest_bar(data))
    	print('smallest:', get_smallest_bar(data))
    	longitude = float(input('Please, enter longitude:'))
    	latitude = float(input('Please, enter latitude:'))
    	print('closest:', get_closest_bar(data, longitude, latitude))
    else:
    	raise NameError('Wrong file type!')

    #print(json.dumps(data, sort_keys=True, indent=2))
    

