import pandas as pd
import re

def parse_text_flight_log(file_path):
    """
    Parse a text-based UAS flight log file and return a pandas DataFrame.
    Args:
        file_path: Path to the text file containing the flight log data
    Returns:
        DataFrame with flight log data organized into rows and columns
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Dictionary to store extracted data
        flight_data = {}
        
        # PILOT & CREW section
        flight_data['Pilot Name'] = extract_value(content, r'Pilot Name:\s*(.+)')
        flight_data['Remote Pilot Cert'] = extract_value(content, r'Remote Pilot Cert #:\s*(.+)')
        flight_data['Visual Observer'] = extract_value(content, r'Visual Observer \(VO\):\s*(.+)')
        flight_data['Flight Operator'] = extract_value(content, r'Flight Operator:\s*(.+)')
        
        # AIRCRAFT & MISSION section
        flight_data['Aircraft Make/Model'] = extract_value(content, r'Aircraft Make/Model:\s*(.+)')
        flight_data['Aircraft Registration'] = extract_value(content, r'Aircraft Registration #:\s*(.+)')
        flight_data['Mission Type'] = extract_value(content, r'Mission Type:\s*(.+)')
        flight_data['Flight Purpose'] = extract_value(content, r'Flight Purpose:\s*(.+)')
        
        # FLIGHT DETAILS section
        flight_data['Date'] = extract_value(content, r'Date:\s*(.+)')
        flight_data['Takeoff Time'] = extract_value(content, r'Takeoff Time:\s*(.+)')
        flight_data['Landing Time'] = extract_value(content, r'Landing Time:\s*(.+)')
        flight_data['Total Flight Time'] = extract_value(content, r'Total Flight Time:\s*(.+)')
        flight_data['Battery Serial'] = extract_value(content, r'Battery Serial:\s*(.+)')
        
        # ENVIRONMENTAL CONDITIONS section
        flight_data['Weather'] = extract_value(content, r'Weather:\s*(.+)')
        flight_data['Wind Speed'] = extract_value(content, r'Wind Speed:\s*(.+)')
        flight_data['Temperature'] = extract_value(content, r'Temperature:\s*(.+)')
        flight_data['Visibility'] = extract_value(content, r'Visibility:\s*(.+)')
        flight_data['GPS Satellites'] = extract_value(content, r'GPS Satellites:\s*(.+)')
        
        # FLIGHT NOTES & MAINTENANCE section
        flight_data['Pre-flight Check'] = extract_value(content, r'Pre-flight check:\s*(.+)')
        flight_data['Notes'] = extract_value(content, r'Notes:\s*(.+)')
        flight_data['Maintenance Required'] = extract_value(content, r'Maintenance Required:\s*(.+)')
        
        # Create DataFrame (single row)
        df = pd.DataFrame([flight_data])
        return df
    
    except Exception as e:
        print(f"Error reading the text file: {e}")
        return None


def extract_value(text, pattern):
    """Helper function to extract values using regex."""
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None
