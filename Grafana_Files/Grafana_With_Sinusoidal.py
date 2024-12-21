# from serial import Serial #--> UNCOMMENT THIS
import socket
import time
import random
import math

measurement = "sensorvals"
measurement2 = "octovals"

field_keys = ["pt1", "pt2", "pt3", "pt4", "pt5", "pt6", "lc1", "lc2"]
random_scale = [random.randint(500, 1000) for _ in range(len(field_keys))]

field_keys2 = ["ignite", "fill", "dump", "vent", "qd", "purge", "mpv", "siren"]


# just in case
def getTime():
    return time.time_ns()


start_time = str(getTime())
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverAddressPort = ("127.0.0.1", 4001)
serverAddressPort2 = ("127.0.0.1", 65415)


def get_sinusoidal_value(max_value: int, current_iteration: int, frequency: int):
    current_x_value = current_iteration / frequency * 2 * math.pi
    return max_value * math.sin(current_x_value)


counter = 0
while True:
    timestamp = str(getTime())

    sensor_data = [
        get_sinusoidal_value(random_scale[i], counter, 30)
        for i in range(len(field_keys))
    ]

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
    counter += 1

    time.sleep(0.5)  # --> COMMENT THIS
