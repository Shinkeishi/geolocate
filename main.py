import requests
import json
import csv

try:

    with open('data/traceroute_output.csv', mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        next(csv_reader)  # Skip the header row

        reading = 1
        list = []
        previous_hop = 0

        # Iterate through the 'name' column and print the names
        for row in csv_reader:
            hop_index = row[2]  # Assuming 'Hop' is the 3rd column (index 2)
            ip_address = row[4]

            # If the website is not in list, remove the website in list and add the website
            # This is to figure out what reading number it is
            if float(hop_index) < float(previous_hop):
                reading += 1

            # Reset previous hop as current hop
            previous_hop = hop_index

            # Assuming 'IP' is the 5th column (index 4)
            request_url = 'https://geolocation-db.com/jsonp/' + ip_address
            response = requests.get(request_url)
            result = response.content.decode()
            result = result.split("(")[1].strip(")")
            result = json.loads(result)
            print(
                f"Reading {reading}: Hop {hop_index}, {result['latitude']}, {result['longitude']}")
            # result contains country_code, country_name, city, postal, latitude, longitude, IPv4, state

except Exception as e:
    print(e)
