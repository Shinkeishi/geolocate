import requests
import json
import csv

try:

    # Initialise variables to write into new CSV file
    reading = ''
    website = ''
    hop = ''
    ip_address = ''
    latitude = ''
    longitude = ''
    location = ''

    # Read trace_route_output.csv file
    with open('data/traceroute_output.csv', mode='r') as file1:
        # Load everything into the new CSV file we created
        with open("data/new_data.csv", mode='a', newline='') as file2:
            csv_writer = csv.writer(file2)
            # Create a CSV reader object
            csv_reader = csv.reader(file1)

            next(csv_reader)  # Skip the header row

            reading = 1
            list = []
            previous_hop = 0

            # Iterate through the 'name' column and print the names
            for row in csv_reader:
                hop = row[2]  # Assuming 'Hop' is the 3rd column (index 2)
                ip_address = row[4]
                website = row[0]

                # If the website is not in list, remove the website in list and add the website
                # This is to figure out what reading number it is
                if float(hop) < float(previous_hop):
                    reading += 1

                # Reset previous hop as current hop
                previous_hop = hop

                # Assuming 'IP' is the 5th column (index 4)
                request_url = 'https://geolocation-db.com/jsonp/' + ip_address
                response = requests.get(request_url)
                result = response.content.decode()
                result = result.split("(")[1].strip(")")
                result = json.loads(result)

                latitude = result['latitude']
                longitude = result['longitude']
                country_name = result['country_name']

                print(
                    f"Reading {reading}: Hop {hop}, Latitude {latitude}, Longitude {longitude}")
                # result contains country_code, country_name, city, postal, latitude, longitude, IPv4, state

                # Write each row of data to the CSV file
                # reading,website,hop,ip,latitude,longitude
                data_list = []
                data_list.append(reading)
                data_list.append(website)
                data_list.append(hop)
                data_list.append(ip_address)
                data_list.append(country_name)
                data_list.append(latitude)
                data_list.append(longitude)

                csv_writer.writerow(data_list)

    print(f"Data has been written to new_data.csv")

except Exception as e:
    print(e)
