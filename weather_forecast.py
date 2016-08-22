import json, urllib3

def header():
	print ("\tCity\t\tTemperature\tDescription")
	print ("=" * 45)

def get_weather_by_city(city_name):

	try:
		http = urllib3.PoolManager()
		r = http.request(
							'GET', 
							'http://api.openweathermap.org/data/2.5/weather',
							fields = {'q':city_name , 'units':'metric', 'appid':'2bc3e79bb974a007818864813f53fd35'}
						)
		data = json.loads(r.data.decode('utf-8'))

		return ("\t{} \t{} \t{}" .format(data['name'].ljust(10), 
										 str(data['main']['temp']).ljust(10), 
										 str(data['weather'][0]['description']).ljust(5))
										)

	except Exception as e:
		print(e)

header()

cities = ['London', 'Nairobi', 'Kampala', 'Lagos', 'Texas', 'Tokyo', 'Sydney']

for city in cities:
	print get_weather_by_city(city)