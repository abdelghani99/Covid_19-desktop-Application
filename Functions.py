import requests
import datetime
import socket
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt

date = datetime.datetime.now()

def return_latest_stats():
    url = "https://api.covid19api.com/summary"
    data = requests.get(url).json()
    return data


def return_realtime_stats_country(country_code):
    country = country_code
    url = "https://api.covid19api.com/total/country/{}".format(country)
    try:
        data = requests.get(url).json()
        size_list = len(data)
        latest_data = int(size_list) - 1
        data_latest = data[latest_data]
    except:
        return None

    return data_latest


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def data_extract(dict):
    data_list = []
    for i, j in dict.items():
        data = {"Final": dict}
    for k, v in data.items():
        #data_list.append(v["Confirmed"])
        data_list.append(v["Deaths"])
        data_list.append(v["Recovered"])
        data_list.append(v["Active"])
        data_list.append(v["Confirmed"])
    return data_list


def Display_pie_chart(data, labels):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("equal")
    ax.pie(data, labels=labels, autopct="%1.2f%%")
    plt.show()
