#added import sys to end program with 'exit'
import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# adding show_graph def to give temperature options#
#plt.style.use('seaborn')
def show_graph(temperatures, graph_title, line_color):
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=line_color)

    # Format plot.
    plt.title(graph_title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#loop for menu instructions, graph plots, and exit
while True:
    print("\n================================================")
    print("This program displays the high/low temperatures") 
    print("of Sitka, Alaska over the span of one year.")
    print("Enter 'highs' to see the high temeratures.")
    print("Enter 'lows' to see the low temperatures.")
    print("Enter 'exit' to quit program.")
    print("================================================")

    choice = input("\nWhat would you like to see?").strip().lower()

    if choice == "highs":
        show_graph(highs, "Daily High Temperatures - 2018", "red")
    elif choice == "lows":
        show_graph(lows, "Daily Low Temperatures - 2018", "blue")
    elif choice == "exit":
        print("Program ended.")
        sys.exit()
    else:
        print("Please enter 'highs', 'lows', or 'exit'.")