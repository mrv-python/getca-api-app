# Invitation PDF Generation

from reportlab.platypus import Paragraph, SimpleDocTemplate, HRFlowable, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Create Invitation PDF file
def create_invite_PDF(guest_data):  
  # Initialize pdf document & flow
  pdf = SimpleDocTemplate("party-invite.pdf",
                        pagesize = letter,
                        rightMargin = inch,
                        leftMargin = inch,
                        topMargin = inch,
                        bottomMargin = inch)
  styles = getSampleStyleSheet()
  flow = []

  # Add content to pdf flow
  # Heading
  text = "You're Invited!"
  flow.append(Paragraph(text, styles["Heading1"]))
  flow.append(HRFlowable(width="100%", thickness=3, color="blue"))
  
  # Party Details
  text = "Join me for a 'Share your Favourite Snack' Party!"
  flow.append(Paragraph(text, styles["Heading3"]))
  flow.append(Spacer(1, 12))
  text = """
    <b>Where:</b> 55 Anywhere Street, Anywhere<br />
    <b>Date:</b> Anydate<br />
    <b>Time:</b> Anytime<br />
  """
  flow.append(Paragraph(text, styles["Normal"]))
  flow.append(Spacer(1, 12))
  text = "Check out what everyone is bringing:"
  flow.append(Paragraph(text, styles["Normal"]))
  for guest in guest_data:
    text = f"- {guest["fave_snack"]} ({guest["name"]})"
    flow.append(Paragraph(text, styles["Normal"]))

  # Closing  
  text = "See you sometime! Or anytime!"
  flow.append(Paragraph(text, styles["Heading4"]))

  # Save PDF
  pdf.build(flow)



