# GETCA GOOGLE API APP DEMO
# Colin Veldkamp, February 2025

import sheets
import invite_pdf
import mail
from google_auth_oauthlib.flow import InstalledAppFlow

def main():
  creds = google_authenticate()
  sheets_service = sheets.get_sheets_service(creds)
  guest_data = sheets.get_guest_data(sheets_service, "GUESTS")
  invite_pdf.create_invite_PDF(guest_data)
  gmail_service = mail.get_gmail_service(creds)
  mail.send_invitations(gmail_service, guest_data)
  

def google_authenticate():
  # Authenticate and connect to Gmail & Sheets API using "credentials.json", return credentials  

  # API SCOPES: If modifying these scopes, delete the file token.json.
  SCOPES = [
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]
  
  creds = None
  
  flow = InstalledAppFlow.from_client_secrets_file(
      "credentials.json", SCOPES
  )
  creds = flow.run_local_server(port=0)

  return creds


# ************************************************ 
# Call main to begin program
# ************************************************ 
if __name__ == "__main__":
  main()
