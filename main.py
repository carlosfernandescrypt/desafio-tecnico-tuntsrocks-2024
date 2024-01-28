# Importing libraries
import pandas as pd
import numpy as np
import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials

num_of_classes = 60

# Use Google credentials to authenticate
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets spreadsheet #
sheet = client.open('Engenharia de Software – Desafio [CARLOS FERNANDES]').sheet1

# Get all values from the spreadsheet #
data = sheet.get_all_values()

# Skip the first two lines #
header_text = data[:3]

# Separate student data #
student_data = data[3:]

# Convert student data to a pandas DataFrame #
df = pd.DataFrame(student_data)

# Get column names #
column = df.columns.tolist()

# Transform grades and absences into decimals #
df[column[2:6]] = df[column[2:6]].apply(pd.to_numeric, errors='coerce')
df[column[3:6]] = df[column[3:6]] / 10

# Define student situation #
df[column[6]] = df.apply(lambda row: 'Reprovado por Falta' if row[column[2]] > (num_of_classes* 0.25) else ('Reprovado por Nota' if row[column[3:6]].mean() < 5 else ('Exame Final' if 5 <= row[column[3:6]].mean() < 7 else 'Aprovado')), axis=1)

# Calculate the final approval score and update the existing column #
df[column[7]] = df.apply(lambda row: 0 if row[column[6]] != 'Exame Final' else math.ceil((10 - row[column[3:6]].mean()) * 2), axis=1)

# Replace NaNs with 0 #
df = df.fillna(0)

# Replace infinities with a large number #
df = df.replace([np.inf, -np.inf], 1e9)

# Save the DataFrame back to Google Sheets #
sheet.update(header_text + df.values.tolist())
