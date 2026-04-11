import matplotlib.pyplot as plt

'''''
this module provides functions to visualize flight data using the matplotlib library.
The plot_flight_durations function creates a line plot of flight durations over time, allowing users
to easily see trends and patterns in the flight data.
'''
def plot_flight_durations(df):
    df = df.sort_values(by="Start_DateTime")

    plt.figure()

    plt.plot(df["Flight_Duration_Min"])
    plt.title("Flight Duration per Flight")
    plt.xlabel("Flight Index")
    plt.ylabel("Duration (minutes)")

    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_duration_histogram(df):
    plt.figure()

    plt.hist(df["Flight_Duration_Min"], bins=10)
    plt.title("Flight Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")

    plt.grid()
    plt.tight_layout()
    plt.show()