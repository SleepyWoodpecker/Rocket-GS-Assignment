from serial import Serial
import socket
import time
import re
import os
import random

measurement = 'sensorvals'

field_keys = ["pt0", "pt1", "pt2", "pt3", "pt4", "pt5", "pt6", "pt7", "pt8", "pt9", "lc1", "lc2"]
octocoupler_keys = ["ignite", "fill", "dump", "vent", "qd", "purge", "mpv", "siren"]


# just in case
def getTime():
    return time.time_ns()

start_time = str(getTime())
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# DO I NEED TO CHANGE SERVER ADDRESS PORT????
pressure_transducer_port = ('127.0.0.1', 4001)
octocoupler_port = ('127.0.0.1', 65415)

# sends data across to the influx DB server
while True:
    timestamp = str(getTime())

    line = f"PT0: {random.randint(800, 1000)}, PT1: {random.randint(800, 1000)}, PT2: {random.randint(800, 1000)}, PT3: {random.randint(800, 1000)}, PT4: {random.randint(200, 300)}, PT5: {random.randint(800, 1000)}, PT6: {random.randint(500, 600)}, PT7: {random.randint(800, 1000)}, PT8: {random.randint(5000, 10000)}, PT9: {random.randint(800, 1000)}, LC1: {random.randint(0, 500)}"
    
    # turn the line into comma-separated values
    line_processing = re.sub(r'[A-Z]+\d: ', '', line)

    data = line_processing.split(', ')

    # Sending data to Grafana as:
    # pt0,pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,lc1,lc2

    # combine all values together, separated by comma
    fields = ''
    for key, val in zip(field_keys, data):
        fields += f'{key}={val},'
    # delete comma after tc2
    fields = fields.strip(',')

    # create influx string
    influx_string = measurement + ' ' + fields + ' ' + timestamp
    print(influx_string)
    UDPClientSocket.sendto(influx_string.encode(), pressure_transducer_port)


    octocoupler_data = [random.randint(0,1) for i in range(len(octocoupler_keys))]
    octocoupler_data_string = ""
    for key, val in zip(octocoupler_keys, octocoupler_data):
        octocoupler_data_string += f'{key}={val},'
    octocoupler_data_string = octocoupler_data_string.strip(",")

    octocoupler_influx_string = "octovals" + ' ' + octocoupler_data_string + ' ' + timestamp
    UDPClientSocket.sendto(octocoupler_influx_string.encode(), octocoupler_port)

    time.sleep(0.5)
