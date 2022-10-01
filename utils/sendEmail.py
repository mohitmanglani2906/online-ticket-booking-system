import os
from dotenv import load_dotenv
load_dotenv()


MAIL_FROM = os.getenv('MAIL_FROM')
MAIL_SUBJECT = "Booking Request"

# def sendEmail(data):
#     mail = MIMEMultipart("alternative")
#     msg = "<html><head></head><body>"
#     for key, value in data.items():
#         msg += key + " : " + value + "<br>"
#         msg += "</body></html>"
#     mail.attach(MIMEText(msg, "html"))
#     mailer = smtplib.SMTP("localhost")
#     output = mailer.sendmail(MAIL_FROM, data['email'], mail.as_string())
#     print(output)
#     mailer.quit()

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmailSendgrid(data):
    show = ''
    showValues = {
        "name": "Name ",
        "email": "Your email id ",
        "sourcePlace": "Your departure place/city/village ",
        "destinationPlace": "Your destination place/city/village ",
        "noOfPassengers": "Total passengers ",
        "date": "Your departure date ",
        "createdAt": "Ticket booking date ",
        "departureTime": "Your Departure Time ",
        "pnrRecords": "Your ticket PNR number "
    }
    msg = "<html><head></head><body>"
    for key, value in data.items():
        if (type(value) == list):
            if key == 'pnrRecords':
                msg += showValues['pnrRecords'] + " : " + " ".join(value) + "<br>"
        else:
            if key == 'name':
                show = showValues['name']
                msg += show + " : " + value + "<br>"
            elif key == 'email':
                show = showValues['email']
                msg += show + " : " + value + "<br>"
            elif key == 'sourcePlace':
                show = showValues['sourcePlace']
                msg += show + " : " + value + "<br>"
            elif key == 'destinationPlace':
                show = showValues['destinationPlace']
                msg += show + " : " + value + "<br>"
            elif key == 'noOfPassengers':
                show = showValues['noOfPassengers']
                msg += show + " : " + value + "<br>"
            elif key == 'date':
                show = showValues['date']
                msg += show + " : " + value + "<br>"
            elif key == 'departureTime':
                show = showValues['departureTime']
                msg += show + " : " + value + "<br>"
            elif key == 'pnrRecords':
                show = showValues['pnrRecords']
                msg += show + " : " + value + "<br>"
        msg += "</body>"
    msg += "<b>Please Note your ticket PNR number</b></html>"
    message = Mail(
        from_email=MAIL_FROM,
        to_emails=data['email'],
        subject='Booking Request',
        html_content=msg)
    try:
        send_grid_key = os.getenv('SEND_GRID_SECRET_KEY')
        sg = SendGridAPIClient(send_grid_key)
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.args)
