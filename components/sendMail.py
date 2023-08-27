import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define path
dir = "CSV"
csv_file = "new_rentals.csv"
# path = os.path.join(dir, csv_file)
path='/home/abhi/Sakila Project/CSV/new_rentals.csv'

# Load credentials from getenv
email_from = os.getenv('email_from')
email_password = os.getenv('email_password')
email_to = os.getenv('email_to')
subject = os.getenv('subject')

# Define Message
message = MIMEMultipart()
message['From'] = email_from
message['To'] = email_to
message['Subject'] = subject
body = 'Attached is the CSV file containing new rentals in the last 1 hour.'
message.attach(MIMEText(body, 'plain'))

def sendMail():
    with open(path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        part.add_header('Content-Disposition', f'attachment; filename= {csv_file}')
        message.attach(part)

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()

    try:
        # Login to the SMTP server
        smtp_server.login(email_from, email_password)

        # Send the email
        smtp_server.sendmail(email_from, email_to, message.as_string())

        print("Email sent successfully.")
        
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")

    finally:
        # Close the SMTP server
        smtp_server.quit()
