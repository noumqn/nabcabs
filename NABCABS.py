# Pre-requiste -> $ pip install -U googlemaps
import googlemaps
from datetime import datetime
from getpass import getpass
# from config import *


'''for importing from config, comment line 5, 8 and lines 21 to 24'''
gmaps = googlemaps.Client(key=getpass('Enter API Key:'))
# gmaps = googlemaps.Client(key=input('Enter API Key:'))
origin = input("Enter origin address: ")
destination = input("Enter destination address: ")


'''
For first 2 kms - Rs.30
For additional kms - Rs.15
'''
# Request directions via drive
now = datetime.now()
directions_result = gmaps.directions(origin,
                                     destination,
                                     mode="driving",
                                     departure_time=now)
# print(directions_result) \


'''change directions_result into directions if importing from config'''


ride_config = directions_result [0]
ride_legs = ride_config['legs'][0]
ride_distance = ride_legs['distance']['value']

'''
total distance = 6800 meters
first 2000 meters = 2000 * 30
remaining distance = (total distance - 2000) * 15

total = first 2000 meters + remaining distance
''' 
final_leg_distance = (ride_distance - 2000)/1000
ride_fare_first_leg = 2 * 30
ride_fare_final_leg = final_leg_distance * 15
total_fare = ride_fare_first_leg + ride_fare_final_leg
print(f'The total fare is: {str(total_fare)} Rs.')
print(f'The total distance is: {str(ride_distance/1000)} KM')
