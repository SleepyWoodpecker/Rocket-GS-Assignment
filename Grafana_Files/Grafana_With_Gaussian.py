# from serial import Serial #--> UNCOMMENT THIS
import socket
import time
import random

measurement = "sensorvals"
measurement2 = "octovals"

field_keys = ["pt1", "pt2", "pt3", "pt4", "pt5", "pt6", "lc1", "lc2"]
field_keys2 = ["ignite", "fill", "dump", "vent", "qd", "purge", "mpv", "siren"]


# just in case
def getTime():
    return time.time_ns()


start_time = str(getTime())
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverAddressPort = ("127.0.0.1", 4001)
serverAddressPort2 = ("127.0.0.1", 65415)


while True:
    timestamp = str(getTime())

    sensor_data = [random.gauss(mu=500, sigma=200) for _ in range(len(field_keys))]

    fields = ""
    for key, val in zip(field_keys, sensor_data):
        fields += f"{key}={val},"
    fields = fields.strip(",")
    influx_string = measurement + " " + fields + " " + timestamp
    print(influx_string)
    UDPClientSocket.sendto(influx_string.encode(), serverAddressPort)

    octocoupler_data = [random.randint(0, 1) for i in range(len(field_keys2))]
    octocoupler_data_string = ""
    for key, val in zip(field_keys2, octocoupler_data):
        octocoupler_data_string += f"{key}={val},"
    octocoupler_data_string = octocoupler_data_string.strip(",")

    octocoupler_influx_string = (
        "octovals" + " " + octocoupler_data_string + " " + timestamp
    )
    UDPClientSocket.sendto(octocoupler_influx_string.encode(), serverAddressPort2)

    time.sleep(1)  # --> COMMENT THIS
