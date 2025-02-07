from serial import Serial
import csv
import time
import socket

PORT = '/dev/tty.usbserial-0001'  # Might need to change this based on your device
BAUDRATE = 9600  # Might need to change this based on your device
ser = Serial(PORT, BAUDRATE, timeout=0.1)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
pressure_transducer_port = ("127.0.0.1", 4001)

def writeToCSV(pt_data, writer):
    # Split pt_data into its components
    pt_data_parts = pt_data.split()  # Split the string by spaces
    
    # The last part is the timestamp, which has no key label
    timestamp = pt_data_parts[-1]  # Last element is the timestamp
    
    # Extract sensor values from the remaining parts (all except the last part)
    sensor_values = pt_data_parts[:-1]
    sensor_values = sensor_values[1].split(",")
    # Extract each sensor value by splitting on the '=' character
    pt1 = sensor_values[0].split("=")[1]
    pt2 = sensor_values[1].split("=")[1]
    pt3 = sensor_values[2].split("=")[1]
    pt4 = sensor_values[3].split("=")[1]
    pt5 = sensor_values[4].split("=")[1]
    pt6 = sensor_values[5].split("=")[1]
    lc1 = sensor_values[6].split("=")[1]
    lc2 = sensor_values[7].split("=")[1]
    
    # Write data to CSV
    writer.writerow([pt1, pt2, pt3, pt4, pt5, pt6, lc1, lc2, timestamp])

def main():
    # Open the CSV file and set up the writer
    with open('sensor_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writerow(['pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'lc1', 'lc2', 'timestamp'])
        
        # Read the data and stream
        while True:
            # Get current timestamp for Grafana to display the data
            current_time = time.time_ns()
            pt_data = ser.readline().decode().strip()
            
            if pt_data.startswith('A') and pt_data.endswith('Z'):
                # Remove the 'A' at the start and 'Z' at the end
                pt_data = pt_data[1:-1]
                
                # Add the timestamp at the end (you can modify this based on your needs)
                pt_data += " " + str(current_time)
                
                # Print the data for verification
                print(pt_data)
                
                # Write data to CSV
                writeToCSV(pt_data, writer)
                
                # Send data via UDP
                UDPClientSocket.sendto(pt_data.encode(), pressure_transducer_port)
            
            # Sleep for a short duration before reading the next value

main()
