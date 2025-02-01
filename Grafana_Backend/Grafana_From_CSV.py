# stream data to grafana at a rate of 10hz, which is once every every 0.1 seconds / 100ms

import csv, time, socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
pressure_transducer_port = ("127.0.0.1", 4001)
octocoupler_port = ("127.0.0.1", 65415)

pt_keys = ["pt0", "pt1", "pt2", "pt3", "pt4", "pt5", "pt6", "pt7", "pt8", "pt9", "lc1"]
pt_channel = "sensorvals"

def main(pt_file: csv.DictReader, thrust_file: csv.DictReader):
    # skip past the header columns
    next(pt_file)
    next(thrust_file)

    # read the data and stream
    while True:
        # get current timestamp so grafana can display the data
        current_time = time.time_ns()

        pt_row = next(pt_file)
        thrust_row = next(thrust_file).split(",")
        pt_row.append(thrust_row[1])
        encoded_pt_data = format_list_to_influx(
            pt_row, pt_keys, pt_channel, current_time
        )
        print(encoded_pt_data)
        UDPClientSocket.sendto(encoded_pt_data, pressure_transducer_port)

        time.sleep(0.1)

def format_list_to_influx(
    data: list[int | float], keys: list[str], channel: str, current_time: int
) -> bytes:
    print(data)
    print(keys)
    data_string = ""
    for key, val in zip(keys, data[1:]):
        data_string += f"{key}={val},"
    data_string = data_string.strip(",")

    return (channel + " " + data_string + " " + str(current_time)).encode()

if __name__ == "__main__":
    with open("../data/pt_values.csv", "r") as pt_csv_file:
        pt_csv = csv.reader(pt_csv_file)

        with open("../data/thrust.csv", "r") as thrust_csv_file:
            main(pt_csv, thrust_csv_file)
