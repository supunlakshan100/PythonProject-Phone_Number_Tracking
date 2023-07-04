from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import phonenumbers
from myNumber import number
from phonenumbers import geocoder

import folium

key = "4787c7902e404df28eec5e0dba74828d"

trackNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(trackNumber, "en")
print(yourLocation)

# get service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(key)

query = str(yourLocation)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

# save map to html file
myMap.save("myLocation.html")
# print(myMap)
