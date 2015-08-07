#!/usr/bin/env python

import os
import json
import collections
import subprocess
import pika #package
import random
import time
import datetime
import dateutil.parser
import requests
from requests.exceptions import ConnectionError

# global variables
speriod = 10
measure_name = "Location"

# get temperature
def get_temp():

    # get coordinates from dump1090
    # ex. MSG,3,111,11111,461F6C,111111,2015/08/07,15:33:39.308,2015/08/07,15:33:39.282,,36050,,,64.64267,25.58407,,,,,,0
    #output = subprocess.Popen(["/usr/local/bin/pcsensor"], stdout=subprocess.PIPE).communicate()[0]
    #output2 = output.split()[4]
    #temperature = output2[:5]
    #print (temperature)
    #temperature = random.uniform(-40, 40)
    lat = random.uniform(64.3, 64.7)
    lon = random.uniform(25.4, 25.6)
    # build json string
    # {
    #     "guid"          :   "string", <- backend takes care.
    #     "organization"  :   "string", <- no need.
    #     "displayname"   :   "string", 
    #     "location"      :   "string",
    #     "measurename"   :   "string",
    #     "unitofmeasure" :   "string",
    #     "value"         :   double/float/integer
 
    objects_list = []
    d = collections.OrderedDict()
    d['displayname'] = "ADS-B"
    d['location'] = "Outside"
    d['measurename'] = measure_name
    d['unitofmeasure'] = ""
    d['value'] = [ lat,lon ]
    d['timestamp'] = str(datetime.datetime.utcnow().isoformat())
    #d['timestampiso'] = dateutil.parser.parse(datetime.datetime.utcnow())
    objects_list.append(d)
    
    json_string = json.dumps(objects_list)
    
    return json_string

def send_temp(message):
    print message
    #uri     = "http://127.0.0.1:3000/log"
    #uri     = "http://nodejslogrestapi-dataalbum.rhcloud.com/log"
    #headers = {'Content-Type' : 'application/json'}
    #try:
    #    res = requests.post(uri, message, headers=headers)
    #    print res.json
    #except ConnectionError as e:
    #    print e
    #    res = "No response"
    
# main function
# This is where the program starts 
def main():
    
    #while True:

        # get temp
        temp=get_temp()

        #send temp
        send_temp(temp)
    
        #time.sleep(speriod)

if __name__=="__main__":
    main()
