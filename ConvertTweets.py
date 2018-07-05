__author__ = 'seandolinar'

import json
import csv
import sys

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''
json_file = sys.argv[1]

data_json = open(json_file, mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object
#data_python = data['tweets']
csv_out = open('tweets_out_ASCII.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

#fields = ['creation', 'tweet', 'location', 'lang'] #field names
fields = ['creation', 'tweet', 'lang', 'country', 'long', 'lat']
writer.writerow(fields) #writes field

for line in data_python:
    def find_null(line, t):
        if line[t] is None:
            return "null"
        else:
            return line.get(t).encode('ascii', 'ignore')

    def find(line, t, r):
        if line[t][r] is None:
            return "null"
        else:
            return line.get(t).get(r).encode('ascii', 'ignore')

    def find_blah(line, t, r, u):
        if line[t][r][u] is None:
            return "null"
        else:
            return line.get(t).get(r).get(u).encode('ascii', 'ignore')
    def find_coor(line, t, r, u):
        if line[t][r][u] is None:
            return "null", "null"
        else:
            coor = line.get(t).get(r).get(u).encode('ascii', 'ignore')
            return coor[0], coor[1]


    # #writes a row and gets the fields from the json object
    # #screen_name and followers/friends are found on the second level hence two get methods
    create = find_null(line, 'created_at')
    text = find_null(line, 'text')
    loc = find(line, 'user', 'location')
    lang = find(line, 'user', 'lang')
    country = find_blah(line, 'user', 'place', 'country_code')
    long, lat = find_coor(line, 'user', 'coordinates', 'coordinates')


    writer.writerow([create,
                     text, #unicode escape to fix emoji issue
                     lang,
                     country,
                     long,
                     lat
                     ])

csv_out.close()
#timestamp, text, lang, userplacecountry_code, "coordinates""coordinates"(array)