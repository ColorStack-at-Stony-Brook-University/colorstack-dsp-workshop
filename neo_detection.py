import requests
import datetime
import json
import random
# Extra
from colorama import Fore

NASA_API = "https://api.nasa.gov/neo/rest/v1/feed"


# Get the date using the datetime
# -------------------------------
current_date = datetime.datetime.now()
current_date = str(current_date)[:10]

# Prepare the requests
# -------------------------------
# Another option is below
# api_string = NASA_API + "?start_date=" + current_date + "&end_date=" + current_date+ "&api_key=your API key"
# response = requests.get(api_string)
arguments = {'start_date':current_date,'end_date':current_date, 'api_key': "your API key"}
response = requests.get(NASA_API,params=arguments)

# Print json
# -------------------------------
neo_data = response.json() # returns a dict version of JSON
# print(json.dumps(neo_data, indent=4, sort_keys=True)) # json.dumps takes in an object and turns it into a JSON formatted string

number_of_neos = neo_data["element_count"]
neo_data = neo_data["near_earth_objects"]
neo_data = neo_data[current_date]
random_num = random.randint(0, number_of_neos-1)

neo = neo_data[random_num]

neo_name = neo["name"]
neo_velocity = neo["close_approach_data"][0]["relative_velocity"]["miles_per_hour"]
neo_min_diameter = neo[ "estimated_diameter"]["miles"]["estimated_diameter_min"]
neo_max_diameter = neo[ "estimated_diameter"]["miles"]["estimated_diameter_max"]
neo_miss_distance = neo["close_approach_data"][0]["miss_distance"]["miles"]
neo_potentially_hazardous = neo["is_potentially_hazardous_asteroid"]
neo_link = neo["nasa_jpl_url"]

print(Fore.GREEN + "Asteroid Name: " + neo_name)
print("Asteroid Velocity: " + neo_velocity + " miles per hour")
print("Asteroid Min Diameter: " + str(neo_min_diameter) + " miles")
print("Asteroid Max Diameter: " + str(neo_max_diameter) + " miles")
print("Asteroid Miss Distance: " + neo_miss_distance + " miles")
print("Asteroid Potentially Hazardous: " + str(neo_potentially_hazardous))
print("NASA JPL Link: " + neo_link)