```.py
import matplotlib.pyplot as plt
from lib import *
import numpy as np

# smoothing data for Remote locations
readings = download_data()

data_4 = get_sensor(readings, 4)
data_5 = get_sensor(readings, 5)

x = []
for i in range(576):
    x.append(i)

x_smooth1, outside_temp_smooth = smoothing(data_5, 12)
x_smooth2, outside_hum_smooth = smoothing(data_4, 12)

# smoothing data for inside the house

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
# smoothing temperature data
x_smooth, room_temp_smooth = smoothing(room_temp, 12)

# room humidity
room_hum = []
for hum_data in room_data:
    hum_datas = hum_data.strip()
    values = hum_datas.split(",")
    humidity = float(values[0])
    room_hum.append(humidity)
# smoothing humidity data
x_smooth, room_hum_smooth = smoothing(room_hum, 12)

# plotting graph
plt.style.use('ggplot')
# room humidity
fig = plt.figure(figsize=(10, 10))
plt.subplot(4, 1, 1)
plt.plot(x_smooth, room_hum_smooth, color="blue")
plt.axhline(y=np.std(room_hum_smooth), color="blueviolet", label="standard deviation")
plt.title("Room humidity")
plt.ylabel("Humidity levels(%)")
plt.tick_params('x', labelbottom=False)
plt.legend(bbox_to_anchor=(0, 1.12, 1, 0.2), loc='lower left', mode="expand", ncol=3)

# room temperature
plt.subplot(4, 1, 2)
plt.plot(x_smooth, room_temp_smooth, color="blue")
plt.axhline(y=np.std(room_temp_smooth), color="blueviolet")
plt.title("Room temperature")
plt.ylabel("Temperature levels(°C)")
plt.tick_params('x', labelbottom=False)

# outside humidity
plt.subplot(4, 1, 3)
plt.plot(x_smooth2, outside_hum_smooth, color="blue")
plt.axhline(y=np.std(outside_hum_smooth), color="purple")
plt.title("Outside humidity")
plt.ylabel("Humidity levels(%)")
plt.tick_params('x', labelbottom=False)

# outside temperature
plt.subplot(4, 1, 4)
plt.plot(x_smooth1, outside_temp_smooth, color="blue")
plt.axhline(y=np.std(outside_temp_smooth), color="purple")
plt.title("Outside temperature")
plt.ylabel("Temperature levels(°C)")
plt.xlabel("Measures")

plt.show()
```
