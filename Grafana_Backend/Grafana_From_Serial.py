from serial import Serial
import csv, time, socket

PORT = '/dev/tty.usbserial-0001'  #might need to change this based on your device
BAUDRATE = 9600 #might need to change this based on your device
ser = Serial(PORT, BAUDRATE, timeout=0.1) 
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
pressure_transducer_port = ("127.0.0.1", 4001)

def main():
    # read the data and stream
    while True:
        # get current timestamp so grafana can display the data
        current_time = time.time_ns()
        encoded_pt_data = ser.readline().decode().strip() + " " + str(current_time)
        UDPClientSocket.sendto(encoded_pt_data.encode(), pressure_transducer_port)
        time.sleep(0.1)

main()
