# GMAIL API INTERACTION

import base64
import sys
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def get_gmail_service(creds):
  # Retrieve GMAIL API Service
  try:
    return build("gmail", "v1", credentials=creds)
  except HttpError as error:
    print(f"An error occured connecting to gmail api: {error}")
    sys.exit()

def get_pdf_attach(filename):
  try:
    with open(filename, "rb") as f:
      pdf_attach = MIMEApplication(f.read(), _subtype="pdf")
    pdf_attach.add_header("Content-Disposition", "attachment", filename=filename)
    return pdf_attach
  except FileNotFoundError as error:
    print(f"Error loading pdf file: {filename} ({error})")
    sys.exit()

def send_invitations(service, guest_data):
  # Send Email to each Guest
  for guest in guest_data:
    # Build Email Message
    message = MIMEMultipart()
    message['to'] = guest["email"]
    message['subject'] = "GETCA Python Session - Demo Email"
    body = get_invite_body(guest)
    message.attach(MIMEText(body, "html"))

    # Add invoice pdf attachment
    message.attach(get_pdf_attach("party-invite.pdf"))

    # Send Message (msg)
    msg = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}  
    message = (service.users().messages().send(userId="me", body=msg).execute())
    print(f"Sent invitation to {guest["name"]} ({guest["email"]})")
    time.sleep(1)

def get_invite_body(guest):
  # Generate Body Email Message using html
  return (
    f"<p>Hello {guest["name"]},</p>"
    f"<h4>Please see a <strong>Party Invitation</strong> attached to this email.</h4>"
    f"<p>Thank you so much for your willingness to share your favourite snack. I'm sure everyone at the party will enjoy {guest['fave_snack']}!"
    f"<p>See you soon...</p>"
    f"<p>Colin</p>"
  )