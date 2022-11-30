import phonenumbers
import config
import opencage
import folium
from phonenumbers import geocoder,carrier,timezone


number = input('enter mobile number starting with +...')

mobileNumber = phonenumbers.parse(number,'CH')

location = geocoder.description_for_number(mobileNumber,'en')

print('location',location)
print(mobileNumber)

from opencage.geocoder import OpenCageGeocode

key=config.opencage_api_key

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save('mylocation.html')