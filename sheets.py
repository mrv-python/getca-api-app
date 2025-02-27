# Google Sheets API Interaction

import os
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# GUEST SHEET ID
SHEET_ID = "1omiFCv3DSfbPReLIJ_BgcyZ_rORJvxFhglZr0-QE1-o"

def get_sheets_service(creds):
  # Retrieve SHEETS API Service

  try:
    service = build("sheets", "v4", credentials=creds)
    sheets = service.spreadsheets() # get all spreadsheets
  except HttpError as error:
    print(f"An error occured connecting to sheets api: {error}")
    sys.exit()

  return sheets

def get_guest_data(sheets_service, query_range):
  # Get Guest Data from Provided Sheet
  
  # Retrieve values from GUESTS Sheet
  result = (
    sheets_service.values()
    .get(spreadsheetId=SHEET_ID, range=query_range)
    .execute()
  )
  values = result.get("values")
    
  # Assemble Guest Data
  guest_data = []
  for i in range(3,len(values)):
    guest = {
      "name": values[i][0],
      "email": values[i][1],
      "fave_snack": values[i][2]
    }
    guest_data.append(guest)

  return guest_data