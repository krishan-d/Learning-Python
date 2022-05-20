import imaplib
import getpass
import email as em

try:
    m = imaplib.IMAP4_SSL('imap.gmail.com')

    # fetch() method should be used to retrieve parts of an email message.
    # print(m.fetch())

    email = getpass.getpass('Email: ')
    password = getpass.getpass('Pass: ')

    m.login(email, password)
    # list() method lists the mailbox names in the specified directory.
    print("List: ", m.list())
    m.select('inbox')

    typ, data = m.search(None, 'SUBJECT "HH"')
    print(typ)
    email_id = data[0]
    result, email_data = m.fetch(email_id, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = em.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == 'text/html':  # text/plain
            body = part.get_payload(decode=True)
            print(body)


except Exception as err:
    print(err)
