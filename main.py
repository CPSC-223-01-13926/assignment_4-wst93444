from weather import *


# file1 = "weather.dat"
filename = "w.dat"
weather = read_data(filename)
mychoice = 0

while True:
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")

    mychoice = int(input("Enter menu choice: "))
    print()

    if mychoice == 1:
        myfile = input("Enter data filename: ")
        # weather = read_data(myfile)
        filename = myfile

    elif mychoice == 2:
        dt = input("Enter date (YYYYMMDD): ")
        tm = input("Enter time (hhmmss): ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter rainfall: "))
        weather[dt + tm] = {"t": t, "h": h, "r": r}
        # write_data(weather, myfile)
        write_data(weather, filename)

    elif mychoice == 3:
        d = input("Enter data: ")
        display = report_daily(weather, d)
        print(display)

    elif mychoice == 4:
        display = report_historical(weather)
        print(display)

    elif mychoice == 9:
        break

########################################## Output ##########################################
# student@tuffix-vm:~/Documents/cpsc 223/assignment_4-wst93444$ python3 main.py 
#       *** TUFFY TITAN WEATHER LOGGER MAIN MENU

# 1. Set data filename
# 2. Add weather data
# 3. Print daily report
# 4. Print historical report
# 9. Exit the program
# Enter menu choice: 1

# Enter data filename: w.dat
#       *** TUFFY TITAN WEATHER LOGGER MAIN MENU

# 1. Set data filename
# 2. Add weather data
# 3. Print daily report
# 4. Print historical report
# 9. Exit the program
# Enter menu choice: 2

# Enter date (YYYYMMDD): 20220107
# Enter time (hhmmss): 133059
# Enter temperature: 82
# Enter humidity: 56
# Enter rainfall: 0.2
#       *** TUFFY TITAN WEATHER LOGGER MAIN MENU

# 1. Set data filename
# 2. Add weather data
# 3. Print daily report
# 4. Print historical report
# 9. Exit the program
# Enter menu choice: 3

# Enter data: 20210203
# ========================= DAILY REPORT ========================
# Date                      Time  Temperature  Humidity  Rainfall
# ====================  ========  ===========  ========  ========
# February 3, 2021      07:55:01           55        87      0.00
# February 3, 2021      09:06:02           63        84      0.00
# February 3, 2021      10:29:03           71        79      0.00
# February 3, 2021      12:55:04           72        69      0.00
# February 3, 2021      18:39:05           59        75      0.00

#       *** TUFFY TITAN WEATHER LOGGER MAIN MENU

# 1. Set data filename
# 2. Add weather data
# 3. Print daily report
# 4. Print historical report
# 9. Exit the program
# Enter menu choice: 4

# ============================== HISTORICAL REPORT ===========================
#                           Minimum      Maximum   Minumum   Maximum     Total
# Date                  Temperature  Temperature  Humidity  Humidity  Rainfall
# ====================  ===========  ===========  ========  ========  ========
# February 3, 2021               55           72        69        87      0.00
# February 5, 2021               57           74        56        68      0.36
# May 17, 2021                   65           82        31        43      0.00
# September 1, 2021              73          101        82        94      0.52
# November 26, 2021              62           73        20        32      0.00
# December 25, 2021              34           46         2        11      0.01
# January 1, 2022                56           56        33        33      0.00
# January 7, 2022                82           82        56        56      0.20

#       *** TUFFY TITAN WEATHER LOGGER MAIN MENU

# 1. Set data filename
# 2. Add weather data
# 3. Print daily report
# 4. Print historical report
# 9. Exit the program
# Enter menu choice: 9

########################################## Output End ##########################################