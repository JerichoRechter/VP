import requests as req
import json
import pandas
import csv


#THIS IS THE FIRST SCRIPT, THIS SCRIPT TAKES A LONG TIME TO FINISH (5-10 mins) SO DON'T PANIC!
#DO NOT FORGET TO READ THE INSTRUCTIONS! IF SCRIPT DOESN'T WORK, IT'S YOUR FAULT!
def get_oauth(): #THIS AUTOMATES ACQUIRING THE FIRST AUTH KEY

    url = "https://api.baubuddy.de/index.php/login"
    payload = {
        "username": "365",
        "password": "1"
    }
    headers = {
        "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
        "Content-Type": "application/json"
    }

    response = req.request("POST", url, json=payload, headers=headers)
    oauth = response.json()['oauth']['access_token']
    token_type = response.json()['oauth']['token_type']
    return(token_type,oauth)

token_type = get_oauth()[0]
oauth = get_oauth()[1]

def get_content(): #THIS IS THE MAIN GET REQUEST FROM THE API
    url = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
    headers = {
        "Authorization": f"{token_type} {oauth}",
        "Content-Type": "application/json"
    }

    response = req.request("GET", url, headers=headers)
    response=response.text

    return(json.loads(response))
def get_colors(id):  #THIS GETS THE COLORS OF THE VEHICLES
                     #DUE TO LACK OF labelIds RESPONSE FROM SERVER, VEHICLE rnr WILL BE USED FOR colorId S!
    url = f"https://api.baubuddy.de/dev/index.php/v1/labels/{id}"
    headers = {
        "Authorization": f"{token_type} {oauth}",
        "Content-Type": "application/json"
    }

    response = req.request("GET", url, headers=headers)
    response = response.text
    easy_response=json.loads(response)
    easy_color=easy_response[0]["colorCode"]

    return (easy_color)
def fill_csv(data_source): #THIS TAKES IN THE FILTERED DATA AND TURNS IT INTO THE FULL VERSION OF THE RESPONSE
    data_file = open('input.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0

    for vehicle in data_source:
        if count == 0:

            header = vehicle.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(vehicle.values())

    data_file.close()
    return()

req_body = get_content()
filtered_req=[]

for vehicle in req_body: #THIS FILTERS THE VEHICLES WITHOUT A VALID HU KEY
    if vehicle["hu"] != "null":
        filtered_req.append(vehicle)


for vehicle in filtered_req: #THIS GETS THE COLOR CODES OF VEHICLES AND ATTACHES THEM TO RELATED VEHICLE,
                             #VEHICLES WITHOUT VALID CODES GET THEIR COLOR SET TO FFFFFF(white)
    try:
        get_colors(filtered_req.index(vehicle))
        key = "colorCode"
        dirty_value = get_colors(filtered_req.index(vehicle))
        value=dirty_value.replace("#", "") #WARNING! API RESPONSE SEND COLOR CODES WITH A # IN FRONT,
                                           # THIS REMOVES THAT SO THE EXCEL CAN RECOGNIZE IT AS A VALID COLOR
        vehicle[key] = value
    except:
        key = "colorCode"
        value = 'ffffff'
        vehicle[key] = value


def sort_csv(*keys,colored):
    #ThIS IS WHERE THE CSV IS SORTED BY GRUPPE! ADD TAGS FROM THE INPUT.CSV TO THE COLUMN
    #COLUMN LIST BELOW, WHICH WILL ADD THOSE TAGS TO IT'S OUTPUT.
    #CHECK THE INPUT.CSV TO SEE ALL THE AVAILABLE TAGS YOU CAN ADD.
    #IF YOU INPUT COLORED AS : colored=True ,YOU WILL GET THE FINAL EXCEL ROWS COLORED BY THE VEHICLE HU DATES.

    column_list = ["rnr","gruppe","colorCode"]
    if colored==True:
        column_list.append("hu")

    for key in keys:
        column_list.append(key)


    df = pandas.read_csv("input.csv", encoding='cp1252')
    df.fillna('#ffffff')
    df = df.sort_values(['gruppe'])
    df[column_list].to_csv('output.csv', index=False)
    df.to_csv('output.csv', columns=column_list, index=False)
fill_csv(filtered_req)
sort_csv(colored=True)




# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath): #THIS WILL RETURN THE ORIGINAL,FILTERED API RESPONSE TO A JSON FILE
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='cp1252') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['rnr']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='cp1252') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code

# Decide the two file paths according to your computer system
csvFilePath ='input.csv'
jsonFilePath ='jsonInput.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)





