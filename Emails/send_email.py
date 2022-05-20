# SMTP(Simple Mail Transfer Protocol) Server:
# Gmail : smtp.gmail.com
# Outlook/ Hotmail : smtp-mail.outlook.com

import smtplib
import getpass

try:
    smtp_ob = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_ob.ehlo()
    smtp_ob.starttls()

    email = getpass.getpass("Email: ")
    # Make 2-step verification on and use app password
    password = getpass.getpass("Pass: ")  # Secure way
    smtp_ob.login(email, password)

    from_address = email
    to_address = email
    sub = input("Subject: ")
    message = input("Message: ")
    msg = "Subject: " + sub + '\n' + message

    smtp_ob.sendmail(from_address, to_address, msg)

    # when msg has already been constructed with addresses for recipients.
    # smtp_ob.send_message(msg)
    print("Success")
except Exception as err:
    print("Error: ", err)
finally:
    smtp_ob.quit()
