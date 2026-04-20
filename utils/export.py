import pandas as pd

def export_data(df, output_path):
    """
    Exports DataFrame to CSV or JSON based on file extension
    """

    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)
        print(f"\nData exported to CSV: {output_path}")

    elif output_path.endswith(".json"):
        df.to_json(output_path, orient="records", indent=4)
        print(f"\nData exported to JSON: {output_path}")

    else:
        print("\nUnsupported file format. Use .csv or .json")

def get_clean_output(df):
    columns = [
        "Start_DateTime",
        "End_DateTime",
        "Flight_Duration_Min"
    ]

    # Include optional fields if they exist
    for col in ["Location", "Purpose"]:
        if col in df.columns:
            columns.append(col)

    return df[columns]