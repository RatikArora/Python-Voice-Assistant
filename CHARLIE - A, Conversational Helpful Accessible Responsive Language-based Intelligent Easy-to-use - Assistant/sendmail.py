import smtplib
from texttovoice import speakandprinttext

def sendmail(text):
    try:
        connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        speakandprinttext("SMTP connection established..\nSending mail")

        mail = "Subject:CHARLIE'S Speech to text program\n\n"+text

        email = "everymondayquotes@gmail.com"
        passw = "txgptkmnbalhtylm"

        connection.login(user=email,password=passw)
        connection.sendmail(from_addr=email,to_addrs="ratikarora007@gmail.com",msg=mail )
        connection.close()
        speakandprinttext("Email Sent")
    except:
        speakandprinttext("couldn't send due to some error")