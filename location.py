import phonenumbers
from phonenumbers import geocoder 
#from test import number
import folium

Key = '68536aa39d3b4a1dace4a347c2bd2f1e'

number=input("Enter a phone number with country code -- ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print("The Location of following number : ",number_location)

from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
results = geocoder.geocode(query)
print("The Latitude and Longitude of the Location is..")
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
