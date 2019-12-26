import zipfile
import time
import sys
import ftplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

inputfile = "location.txt"
outputfile = "log.txt"

try:
    filein = open(inputfile, mode='r', encoding='utf_8')
    fileout = open(outputfile, mode='a', encoding='utf_8')
except:
    answ = " Can not read location." + str(sys.exc_info()[1])
else:
    answ = " Location OK."
finally:
    try:
        name_archive = str(time.strftime("%Y%m%d-%H%M%S")) + ".zip"
        zip_archive = zipfile.ZipFile(name_archive, 'w')
        for n, line in enumerate(filein, 1):
            zip_archive.write(line.strip(), compress_type=zipfile.ZIP_DEFLATED)
        zip_archive.close()
    except:
        answ = answ + " Can not create archive." + str(sys.exc_info()[1])
    else:
        answ = answ + " Archive with " + str(n) + " file Ok."
    finally:
        try:
            connect = ftplib.FTP('192.168.43.1')
            connect.FTP.connect(host='192.168.43.1', port=2221)

            connect.cwd("/Laptop/")
            location = "D:/Git/Turk/" + name_archive
            ar = open(location, mode='rb')
            connect.storbinary("STOR " + name_archive, ar)
            ar.close()
        except:
            answ = answ + " Can not send archive." + str(sys.exc_info())
        else:
            answ = answ + " Network Ok."

try:
    mail_sender = 'adbfgbc45@gmail.com'
    mail_receiver = 'sashok333.111@gmail.com'
    username = mail_sender
    password = '12dfhhhauj'
    server = smtplib.SMTP('smtp.gmail.com:587')
    subject = u'Log ' + mail_sender
    body = u'Laptop log ' + answ
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    #server.starttls()
    #server.ehlo()
    #server.login(username, password)
    #server.sendmail(mail_sender, mail_receiver, msg.as_string())
    #server.quit()
except:
    answ = answ + " Can not send email." + str(sys.exc_info()[1])
else:
    answ = answ + " Email Ok."

fileout.write(str(time.strftime("%Y%m%d-%H%M%S")) + answ + ' \n')
filein.close()
fileout.close()
