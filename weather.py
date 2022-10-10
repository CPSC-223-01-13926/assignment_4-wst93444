from dataclasses import dataclass
import json
import calendar


def read_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]["t"] > x:
                x = data[key]["t"]
    return x


def min_temperature(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]["t"] < x:
                x = data[key]["t"]
    return x


def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] > x:
                x = data[key]["h"]
    return x


def min_humidity(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] < x:
                x = data[key]["h"]
    return x


def tot_rain(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            x += data[key]["r"]
    return x


def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display = (
        display + "Date                      Time  Temperature  Humidity  Rainfall\n"
    )
    display = (
        display + "====================  ========  ===========  ========  ========\n"
    )
    for key in data:
        if date == key[0:8]:
            m = (
                calendar.month_name[int(date[4:6])]
                + " "
                + str(int(date[6:8]))
                + ", "
                + str(int(date[0:4]))
            )
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]["t"]
            h = data[key]["h"]
            r = data[key]["r"]
            display = display + f"{m:22}{tm:8}{t:13}{h:10}{r:10.2f}\n"
    return display


def report_historical(data):
    display = (
        "============================== HISTORICAL REPORT ===========================\n"
    )
    display += (
        "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    )
    display += (
        "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    )
    display += (
        "====================  ===========  ===========  ========  ========  ========\n"
    )
    temp = None
    for key in data:
        date = key[0:8]
        if temp == date:
            continue
        m = (
            calendar.month_name[int(date[4:6])]
            + " "
            + str(int(date[6:8]))
            + ", "
            + str(int(date[0:4]))
        )
        min_t = min_temperature(data, date)
        max_t = max_temperature(data, date)
        min_h = min_humidity(data, date)
        max_h = max_humidity(data, date)
        total_r = tot_rain(data, date)
        display += f"{m:20}{min_t:13}{max_t:13}{min_h:10}{max_h:10}{total_r:10.2f}\n"
        temp = date
    return display
