import urllib3,urllib2 ,json


city_name = ['Nairobi','Lagos', 'London', 'Khartom', 'Tel aviv','Kampala','Bagdad', 'Cairo']

def get_details(city_name):

	'''
	program that desplay weather condition
	'''

	http = urllib3.PoolManager()
	base_url = 'http://api.openweathermap.org/data/2.5/weather'
	api = "2bc3e79bb974a007818864813f53fd35"
	request = http.request( 'GET',base_url,
		fields = {
		'q': city_name,
		'units': 'metric',
		'appid': api
		
		})
	response = json.loads(request.data.decode('utf-8'))
	# format the output
	return '{} {}'.format(str(response ['weather'][0]['description']).ljust(15), str(response['main']['temp'] ).rjust(15))
print (' descriptions          temperature       city  \n ' + "=" *50)	
# loop in the cites
for city in city_name:    
	print   get_details(city), city.rjust(15 )


