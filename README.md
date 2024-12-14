# Create Your Own Email Bot

Tired of manually writing hundreds of emails? With just 8 lines of Python code, you can create an Email Bot to send emails automatically.

Follow these simple steps to build your Email Bot.

Prerequisites
Step 1: Configure Your Gmail Account
To allow your bot to send emails using your Gmail account:

Open Gmail and check your inbox for a security email about someone trying to access your account.
Follow these steps to enable "Less Secure App Access":
Click on the three dots in your browser's URL bar and select "Manage Your Google Account."
In the left-side panel, click on "Security."
Scroll down to find "Less Secure App Access."
Click "Turn On Access" and enable the feature.
Now your Email Bot can use your Gmail account securely.
Writing the Email Bot
Import the Required Library

Use Python's built-in smtplib library for sending emails.

import smtplib
Set Up the SMTP Server

Define the SMTP server details and initialize the connection.

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Encrypt the connection using TLS
Log in to Your Email Account

Use your Gmail address and app password for authentication.

server.login('YOUR_EMAIL_ADDRESS', 'YOUR_EMAIL_PASSWORD')
Send the Email

Use the sendmail method to send the email with the sender's address, recipient's address, and message.

server.sendmail('SENDER_EMAIL_ADDRESS', 
                'RECIPIENT_EMAIL_ADDRESS', 
                'YOUR_MESSAGE')
Full Code Example
Here's the complete 8-line Python code for your Email Bot:

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('YOUR_EMAIL_ADDRESS', 'YOUR_EMAIL_PASSWORD')
server.sendmail('SENDER_EMAIL_ADDRESS',
                'RECIPIENT_EMAIL_ADDRESS',
                'YOUR_MESSAGE')
server.quit()
Features:
Efficient: Send emails automatically in seconds.
Customizable: Modify the recipient list and message content as needed.
Simple: Just a few lines of code!
Notes:
Replace placeholders (YOUR_EMAIL_ADDRESS, etc.) with actual values.
Always protect your email credentials. Use environment variables or encrypted storage if sharing or deploying the code.
Now your Email Bot is ready! 🎉 Enjoy automating your emails effortlessly!
