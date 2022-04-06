import smtplib
from email.message  import EmailMessage
from random import randint

def sendMail(msg):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login()
    server.send_message(msg)
    server.quit()

def mail(toEmail):
    code = randint(100000, 999999)
    message = EmailMessage()
    message["Subject"] = "OTP verification from Team passWd"
    message["From"] = "Team passWd"
    message['To'] = toEmail
    message.set_content(
        f"""
            Enter the code:
                {code}
            To verify your Email 
            
                                            Thank You
                                            Team passWd
        """
    )
    sendMail(message)
    return code
    
    