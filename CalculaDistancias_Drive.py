# Code for connecting to google maps and getting distance and duration
# between x and y
# June 6, 2019

# Requirement: python2.7
# From the terminal, run:
# pip install gmaps
# pip install googlemaps
# pip install Client
# (in some cases pip2 runs instead of pip)

# Import packages:
import googlemaps
import csv
from datetime import datetime
# Set the active key from the google maps API
gmaps = googlemaps.Client(key='enter key here')
# Set path of the input file, read it and call it "lines". This path will be
# where the output file will be created

import os
import fileinput
path=      'enter path'
index= 1
for root, dirs, files in os.walk(path):
   for fname in files:
       fp ='D:{fname}'.format(fname=fname)
       lines = open(fp).read().splitlines()
       # Create parameter of time and array for output storing
       now = datetime.now()
       dist = []
       # Create csv output file
       name = os.path.basename("{index}".format(index=fname))
       name = os.path.splitext(name)[0]
       name = "{name1}.csv".format(name1=name)
       
       f = open(name,'w')
       with f:
           writer = csv.writer(f,delimiter=',')
           writer.writerow(['drive_distance','drive_time'])
           # Calculate direction outputs
           #   for row in range(len(lines)):
           for i in range(len(lines)):
               x=lines[i].split()[0] # GPS address 1
               y=lines[i].split()[1] # GPS address 2
               directions_result = gmaps.directions(x,y,
                                                    mode = "driving",
                                                    avoid = "ferries",
                                                    departure_time = now
                                                    )
               # Store results
               driv_dist =  (directions_result[0]['legs'][0]['distance']['text'])
               driv_time = (directions_result[0]['legs'][0]['duration']['text'])
               # Write results in output file
               writer.writerow([driv_dist,driv_time])
               index = index +1
            # Open the path and check for file "result.csv"
