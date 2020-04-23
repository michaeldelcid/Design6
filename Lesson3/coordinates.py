#Displays coordinates of a well known location
#Does not display coordinates of locations with the same name

import sys
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
address = sys.argv[1]
location = geolocator.geocode(address)
print(location.address)
print((location.latitude, location.longitude))
#print(location.raw)
