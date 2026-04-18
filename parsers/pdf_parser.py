import pdfplumber
import re
import pandas as pd

def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text

"""
split entries by date pattern (MM/DD/YYYY), then extract date, location, duration, and purpose using regex and string manipulation.
The function returns a DataFrame with the extracted information.
"""
def parse_pdf_to_dataframe(text):
    # Split entries by date pattern
    entries = re.split(r'(?=\d{1,2}/\d{1,2}/\d{4})', text)

    data = []

    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        # Extract date
        date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', entry)
        date = date_match.group() if date_match else None

        # Extract duration
        duration_match = re.search(
            r'(\d+\s*Hours?(?:,\s*\d+\s*Minutes?)?|\d+\s*Minutes?)',
            entry
        )
        duration = duration_match.group() if duration_match else None

        # Extract purpose (after duration)
        purpose = None
        if duration:
            parts = entry.split(duration)
            if len(parts) > 1:
                purpose = parts[1].strip()

        # Extract location (between date and duration)
        location = None
        if date and duration:
            try:
                location = entry.split(date)[1].split(duration)[0].strip()
            except:
                location = None

        data.append({
            "Date": date,
            "Location": location,
            "Raw_Duration": duration,
            "Purpose": purpose
        })

    return pd.DataFrame(data)