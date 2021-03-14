def email():
    import smtplib
    import ssl
    from email.mime.text import MIMEText
    from email.utils import formataddr
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase  
    from email import encoders  
    import csv 

    # fill Path of csv file
    csv_filepathname="/home/garvit/send-mail-python/excel.csv" 
    
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
    
    filename="image.png"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())    
    
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment; filename= {}".format(filename),)
    
    # User configuration and enter detail(email address and password)
    sender_email = "Email"
    sender_name = "<<Sender Name>>"
    password = "Password"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Encrypts the email
    context = ssl.create_default_context()
    server.starttls()

    # We log in into our Google account
    server.login(sender_email, password)
    
    for i in dataReader:
        username = i[0].title()
        email = i[1]
            
        print(username,email)
        print("Sending the email...")
        
        # Configurating user's info
        msg = MIMEMultipart('alternative')
        msg['To'] = formataddr((username, email))
        msg['From'] = formataddr((sender_name, sender_email))

        # fill Subject of mail
        msg['Subject'] = "Send Bulk Mail"
        
        # HTML content of mail
        html = """\
            <h1>Hi {username} </h1>""".format(username=username)

        # Turn these into plain/html MIMEText objects
        part2 = MIMEText(html, "html")
        
        msg.attach(part2)
        
        # Attaching Image    
        msg.attach(part)

        try:
            toEmail=[email]
            server.sendmail(sender_email,toEmail, msg.as_string())
            print('Email sent!')
        except Exception as e:
            print("Oh no! Something bad happened!n{e}".format(e=e))
            break
        # finally:
        #     print('Closing the server...')
        #     server.quit()	         