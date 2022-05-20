# Text download:
# import urllib2
# response = urllib2.urlopen('https://wordpress.org/plugins/about/readme.txt')
# data = response.read()
# print(data)

# # HTML download:
# response = urllib2.urlopen('https://en.wikipedia.org/')
# html = response.read()
# print(html)


import ftplib
import sys


def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except:
        print("Error")


ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")

ftp.cwd('/pub/')
getFile(ftp, 'README.nluug')

ftp.quit()
