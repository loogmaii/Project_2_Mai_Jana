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

# linear model
m2, b2 = np.polyfit(x_smooth1, outside_hum_smooth, 1)
x_model2 = [1, 576]
y_model2 = []
for i in x_model2:
    y_model2.append(m2 * i + b2)

m3, b3 = np.polyfit(x_smooth2, outside_temp_smooth, 1)
x_model3 = [1, 576]
y_model3 = []
for i in x_model3:
    y_model3.append(m3 * i + b3)

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

# linear model
m, b = np.polyfit(x_smooth, room_hum_smooth, 1)
x_model = [1, 577]
y_model = []
for i in x_model:
    y_model.append(m * i + b)

m1, b1 = np.polyfit(x_smooth, room_temp_smooth, 1)
x_model1 = [1, 577]
y_model1 = []
for i in x_model1:
    y_model1.append(m1 * i + b1)

# plotting graph
plt.style.use('ggplot')
# room humidity
fig = plt.figure(figsize=(10, 10))
plt.subplot(4, 1, 1)
plt.plot(x_smooth, room_hum_smooth, color="blue")
plt.plot(x_model, y_model, color="red")
plt.title("Room humidity")
plt.ylabel("Humidity levels(%)")
plt.tick_params('x', labelbottom=False)

# room temperature
plt.subplot(4, 1, 2)
plt.plot(x_smooth, room_temp_smooth, color="blue")
plt.plot(x_model1, y_model1, color="red")
plt.title("Room temperature")
plt.ylabel("Temperature levels(°C)")
plt.tick_params('x', labelbottom=False)

# outside humidity
plt.subplot(4, 1, 3)
plt.plot(x_smooth2, outside_hum_smooth, color="blue")
plt.plot(x_model2, y_model2, color="red")
plt.title("Outside humidity")
plt.ylabel("Humidity levels(%)")
plt.tick_params('x', labelbottom=False)

# outside temperature
plt.subplot(4, 1, 4)
plt.plot(x_smooth1, outside_temp_smooth, color="blue")
plt.plot(x_model3, y_model3, color="red")
plt.title("Outside temperature")
plt.ylabel("Temperature levels(°C)")
plt.xlabel("Measures")

plt.show()
```
