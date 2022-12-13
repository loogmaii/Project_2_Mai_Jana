```.py
import matplotlib.pyplot as plt
from lib import *

# raw data inside the house
# reading file lines
with open("data.csv", "r") as file:
    room_data = file.readlines()

# room temperature
room_temp = []
for temp_data in room_data:
    temp_datas = temp_data.strip()
    values = temp_datas.split(",")
    temperature = float(values[1])
    room_temp.append(temperature)

# room humidity
room_hum = []
for hum_data in room_data:
    hum_datas = hum_data.strip()
    values = hum_datas.split(",")
    humidity = float(values[0])
    room_hum.append(humidity)

x_values = []
for i in range(len(room_temp)):
    x_values.append(i)

# raw data for Remote locations

readings = download_data()

data_4 = get_sensor(readings, 4)
data_5 = get_sensor(readings, 5)

data_4 = data_4[0:576]
data_5 = data_5[0:576]

#plotting the data
x = []
for i in range(576):
    x.append(i)

# plotting graph
plt.style.use('ggplot')
# humidity
fig = plt.figure(figsize=(10,10))
plt.subplot(4, 1, 1)
plt.plot(x_values, room_hum, color="blue")
plt.title("Room humidity")
plt.ylabel("Humidity levels (%)")
plt.tick_params('x', labelbottom=False)

# temp
plt.subplot(4, 1, 2)
plt.plot(x_values, room_temp, color="blue")
plt.title("Room temperature")
plt.ylabel("Temperature levels(°C)")
plt.tick_params('x', labelbottom=False)

plt.subplot(4, 1, 3)
plt.plot(x, data_4, color="blue")
plt.title("Outside humidity")
plt.ylabel("Humidity levels(%)")
plt.tick_params('x', labelbottom=False)

plt.subplot(4, 1, 4)
plt.plot(x, data_5, color="blue")
plt.title("Outside temperature")
plt.xlabel("Samples")
plt.ylabel("Temperature levels(°C)")

plt.show()
```
