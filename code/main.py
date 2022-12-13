```.py
from datetime import datetime
import pyfirmata
from pyfirmata import Arduino
import csv
import serial
import time


arduino = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) # port of the arduino
def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data

num_temperature = []
num_humidity = []
num_time = []

data = {
    'hum': [],
    'tem': [],
}

while True:
    time.sleep(300)
    value = read()
    msg = value.decode("utf")
    msg = msg.strip()
    if not 'Hello' in msg:

        messages = msg.split(" ")
        hum_str = messages[0].split(":")[1]
        tem_str = messages[1].split(":")[1]
        hum = float(hum_str[0:-1])
        tem = float(tem_str[0:-1])


        with open("data.csv","a") as file:
            dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"{hum},{tem},{dt_string}\n")

        data["hum"].append(hum)
        data["tem"].append(tem)

    print(data)
```
