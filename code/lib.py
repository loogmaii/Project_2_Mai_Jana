```.py
import requests


def get_sensor(readings: list, id: int) -> list:
    data = []
    for i in readings:
        if i['sensor_id'] == id and i['id'] > 38820 and i['id'] < 53070:
            data.append(i['value'])
    return data


def download_data(url: str = "192.168.6.142/readings") -> list:
    req = requests.get(f"http://{url}")
    readings = req.json()['readings'][0]
    return readings


def smoothing(data: list, size_window: int = 12):
    data_smooth = []
    x = []
    for i in range(0, (len(data) - 6), size_window):
        data_in_window = data[i:i + size_window]
        average = sum(data_in_window) / size_window
        data_smooth.append(average)
        x.append(i)
    return x, data_smooth
  ```
