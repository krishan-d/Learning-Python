# Network Programming :

# Socket Programming
# Client Programming
# Web Servers
# Web Scrapping
# Web Frame works
# Getting Geo Locations


# Internet Protocol:
# HTTP : urllib.request
# Opening the HTTP URL.
# HTTP : urllib.response
# Create a response object for url request.
# HTTP : urllib.parse
# To break Uniform Resource Locator (URL) strings up in components like (addressing scheme, network location, path etc.)
# HTTP : urllib.robotparser
# Finds out whether a particular user agent can fetch a URL on the Website that published the robots.txt file.

# FTP : ftplib
# Implements the client side of the FTP protocol.
# POP : poplib
# Defines a class, POP3, which encapsulates a connection to a POP3 server to read messages from  email server.
# IMAP : imaplib
# Defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, encapsulate a connection to an IMAP4 server to read emails.
# SMTP	smtplib
# Defines an SMTP client session object, can be used to send mail to any Internet machine with an SMTP listener demon.
# Telnet : telnet
# This module provides a Telnet class that implements the Telnet protocol to access a server through telnet.


# IP Address:
import ipaddress

# Validate IPV4 Address:
# Value range(0-255), beyond range throws Error.
import flask as flask

print(ipaddress.ip_address(u'192.168.0.255'))

# Validate IPV6 Address:
# Value range(0-FFFF), beyond range throws Error.
print(ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))

# IP Address Arithmetic:
print(ipaddress.IPv4Address(u'192.168.0.2')+1)



