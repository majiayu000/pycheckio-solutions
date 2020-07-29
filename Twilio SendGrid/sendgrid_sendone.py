#!/usr/bin/env checkio --domain=py run sendgrid-sendone

# To solve this mission you must use theSendGrid API Key(this video will explainhow to create your own API Key). Check out thesePython examples.
# 
# It all starts with your first email. Let’s try to send one.
# 
# Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.
# 
# Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)
# 
# Input:Two arguments: email and a username.
# 
# Output:None. You should send an email. You don’t need to return anything.
# 
# 
# send_email('a.lyabah@checkio.org', 'oduvan')
# send_email('somebody@gmail.com', 'Some Body')
# 
# END_DESC

import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    message = Mail(
    from_email='1835304752@qq.com  ',
    to_emails=email,
    subject='Welcome',
    plain_text_content=BODY.format(name)
    )
    response = sg.send(message)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    send_email('mylifcc@gmail.com', 'Some Body')
    print('Done')