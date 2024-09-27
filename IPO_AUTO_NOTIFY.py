import re
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# URL of the web page
web_path = "https://www.investorgain.com/report/live-ipo-gmp/331/ipo/"

# Function to get and parse the HTML content
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve content, status code: {response.status_code}")

# Extract table from the HTML
def extract_table(url):
    html_content = get_html_content(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the table by its id
    table = soup.find('table', {'id': 'mainTable'})
    
    # Extract headers
    headers = [header.text for header in table.find_all('th')]
    
    # Extract rows
    data = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)
    return df

# Data Processing and Cleaning
def process_ipo_data(df):
    # Strip whitespace from column headers
    df.columns = df.columns.str.strip()

    # Select required columns (no view/copy issues here)
    df = df[['IPO', 'Price', 'Est Listing', 'IPO Size', 'Open', 'Close', 'BoA Dt', 'Listing']].copy()
    
    # Add current year to Open and Close dates
    today = datetime.today()
    current_year = today.year
    
    # Use .loc[] to avoid SettingWithCopyWarning
    df.loc[:, 'Open'] = df['Open'] + '-' + str(current_year)
    df.loc[:, 'Close'] = df['Close'] + '-' + str(current_year)
    
    # Convert dates to datetime format
    df.loc[:, 'Open'] = pd.to_datetime(df['Open'], format='%d-%b-%Y')
    df.loc[:, 'Close'] = pd.to_datetime(df['Close'], format='%d-%b-%Y')
    
    # Filter IPOs that haven't closed yet
    df = df[df['Close'] >= today].copy()
    
    # Rename columns for clarity
    df.rename(columns={'BoA Dt': 'Allotment Date'}, inplace=True)
    
    # Extract IPO names without the "IPO" suffix
    df['IPO_Name'] = df['IPO'].apply(lambda x: re.search(r'(.*?)IPO', x).group(1).strip() if 'IPO' in x else x)
    
    return df


# Function to generate IPO dictionary
def generate_ipo_dict(df):
    ipo_dict = {}
    for index, row in df.iterrows():
        ipo_data = {
            'IPO Name': row['IPO_Name'],
            'GMP': row['Est Listing'],
            'IPO Size': row['IPO Size'],
            'Open Date': row['Open'].strftime('%d-%m-%Y'),
            'Close Date': row['Close'].strftime('%d-%m-%Y')
        }
        ipo_dict[row['IPO_Name']] = ipo_data
    return ipo_dict

import pprint

# Main execution flow
if __name__ == "__main__":
    df = extract_table(web_path)
    
    # Show actual columns after extraction
    print("Extracted columns:", df.columns)
    
    # Process the data
    processed_df = process_ipo_data(df)
    
    # Display DataFrame in readable format
    print("\n=== Processed IPO Data ===")
    print(processed_df.to_string(index=False))  # Display without row indices for cleaner output
    
    # Generate IPO dictionary
    ipo_dict = generate_ipo_dict(processed_df)
    
    # Use pprint to display the dictionary in readable format
    print("\n=== IPO Dictionary ===")
    pprint.pprint(ipo_dict, indent=4)  # Pretty print the IPO dictionary

