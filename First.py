import zipfile
import time
import sys
import ftplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

inputfile = "location.txt"
logfile = "log.txt"

try:
    filein = open(inputfile, mode="r", encoding="utf_8")
    fileout = open(logfile, mode="a", encoding="utf_8")
except:
    answ = " Can not read location." + str(sys.exc_info()[1])
else:
    answ = " Location OK."
finally:
    try:
        name_archive = str(time.strftime("%Y%m%d-%H%M%S")) + ".zip"
        zip_archive = zipfile.ZipFile(name_archive, "w")
        for n, line in enumerate(filein, 1):
            zip_archive.write(line.strip(), compress_type=zipfile.ZIP_DEFLATED)
        zip_archive.close()
    except:
        answ = answ + " Can not create archive." + str(sys.exc_info()[1])
    else:
        answ = answ + " Archive with " + str(n) + " file(s) Ok."
    finally:
        try:

            def upload(ftp, file):
                ext = os.path.splitext(file)[1]
                if ext in (".txt", ".htm", ".html", "jks"):
                    ftp.storlines("STOR " + file, open(file))
                else:
                    ftp.storbinary("STOR " + file, open(file, "rb"))

            connect = ftplib.FTP("127.0.0.1")
            connect.login("Alex", "1q1q")
            upload(connect, name_archive)
            #connect.FTP.connect(port=21)
            #connect.cwd("/Laptop/")
            #connect.storbinary("STOR " + name_archive, open(name_archive, "rb"))
            #name_archive.close()
        except:
            answ = answ + " Can not send archive." + str(sys.exc_info())
        else:
            answ = answ + " Network Ok."

try:
    mail_sender = "adbfgbc45@gmail.com"
    mail_receiver = "sashok333.111@gmail.com"
    username = mail_sender
    password = "12dfhhhauj"
    server = smtplib.SMTP("smtp.gmail.com:587")
    subject = u"Log " + mail_sender
    body = u"Laptop log " + answ
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    #server.starttls()
    #server.ehlo()
    #server.login(username, password)
    #server.sendmail(mail_sender, mail_receiver, msg.as_string())
    #server.quit()
except:
    answ = answ + " Can not send email." + str(sys.exc_info()[1])
else:
    answ = answ + " Email Ok."

fileout.write(str(time.strftime("%Y%m%d-%H%M%S")) + answ + " \n")
filein.close()
fileout.close()
