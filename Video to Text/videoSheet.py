import os
import requests
import sys

def getGoogleSheet(spreadsheet_id, outFile):
    # Construct the Google Sheets export URL
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'

    # Make the HTTP request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the current working directory
        current_dir = os.getcwd()

        # Construct the file path in the current directory
        filepath = os.path.join(current_dir, outFile)

        # Save the CSV content to the file
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f'CSV file saved to: {filepath}')
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')
        sys.exit(1)

# Example usage
spreadsheet_id = '1QGxWpxkT-I2_UocEcHBCmN4Y91EfUdqrhc9pEXBlJeo'
output_file = 'output.csv'
getGoogleSheet(spreadsheet_id, output_file)

sys.exit(0)  # success