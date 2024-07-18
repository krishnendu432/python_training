#This script has been created for to send automatic mail
import smtplib # Import 'smtplib' library package
hostname='smtp.gmail.com'
username='ghosh1.roy@gmail.com'
password='ybobbspjyizkyruu'
with smtplib.SMTP(host=hostname) as connection:
    connection.starttls() # Open transport layer security
    connection.login(user=username, password=password)
    connection.sendmail(
        from_addr=username,
        to_addrs=username,
        msg=f'Subject: Python mail send script\n\n This is a test mail from python'
    )
