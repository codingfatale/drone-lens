import pandas as pd
import matplotlib.pyplot as plt


''''
This module provides a function to parse CSV files using the pandas library. 
The parse_csv function reads a CSV file and returns a DataFrame object, which is a powerful data
'''

def parse_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None
