import smtplib
import config

from email.mime.text import MIMEText

message = '<html><body> <b>hello world</b> </body></html>'




def send_email(to_email, subject, msg):
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        my_email = MIMEText(msg, "html")
        my_email["From"] = config.EMAIL_ADDRESS
        my_email["To"] = to_email
        my_email["Subject"] = subject

        server.sendmail(config.EMAIL_ADDRESS, to_email, my_email.as_string())
        server.quit()
    except Exception as woo:
        print(woo)