import pandas as pd

def calculate_flight_metrics(df):
    """
    Cleans dataset and calculates flight duration
    """

    # Clean column names (remove leading/trailing spaces)
    df.columns = df.columns.str.strip()

    # Combine Start Date + Start Time
    df["Start_DateTime"] = pd.to_datetime(
        df["Start Date:"] + " " + df["Start Time:"],
        errors="coerce"
    )

    # Combine End Date + End Time
    df["End_DateTime"] = pd.to_datetime(
        df["End Date:"] + " " + df["End Time:"],
        errors="coerce"
    )

    # Calculate duration (minutes)
    df["Flight_Duration_Min"] = (
        df["End_DateTime"] - df["Start_DateTime"]
    ).dt.total_seconds() / 60

    # Remove bad data (negative or missing durations)
    df = df[df["Flight_Duration_Min"] > 0]

    return df


def summarize_flights(df):
    return {
        "Total Flights": len(df),
        "Total Flight Time (min)": round(df["Flight_Duration_Min"].sum(), 2),
        "Average Flight Time (min)": round(df["Flight_Duration_Min"].mean(), 2),
        "Max Flight Time (min)": round(df["Flight_Duration_Min"].max(), 2),
    }