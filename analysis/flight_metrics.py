import pandas as pd
import re

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

def convert_duration_to_minutes(duration_str):
    """
converts duration strings like "1 Hour, 30 Minutes" or "45 Minutes" to total minutes as a float.
If the input is None or cannot be parsed, it returns None.
for pdf parsing
"""
    # Handle NaN / None
    if pd.isna(duration_str):
        return None

    # Ensure string
    duration_str = str(duration_str).strip()


    if duration_str is None:
        return None

    hours = 0
    minutes = 0

    # Extract hours
    hour_match = re.search(r'(\d+)\s*Hour', duration_str, re.IGNORECASE)
    if hour_match:
        hours = int(hour_match.group(1))

    # Extract minutes
    minute_match = re.search(r'(\d+)\s*Minute', duration_str, re.IGNORECASE)
    if minute_match:
        minutes = int(minute_match.group(1))

    return hours * 60 + minutes

def add_pdf_duration(df):
    """
    Adds Flight_Duration_Min column from Raw_Duration
    """
    # Optional: normalize column first
    df["Raw_Duration"] = df["Raw_Duration"].fillna("")

    # Apply conversion
    df["Flight_Duration_Min"] = df["Raw_Duration"].apply(convert_duration_to_minutes)

    # Remove invalid rows
    df = df[df["Flight_Duration_Min"].notna()]
    return df


def summarize_flights(df):
    return {
        "Total Flights": len(df),
        "Total Flight Time (min)": round(df["Flight_Duration_Min"].sum(), 2),
        "Average Flight Time (min)": round(df["Flight_Duration_Min"].mean(), 2),
        "Max Flight Time (min)": round(df["Flight_Duration_Min"].max(), 2),
    }