import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('YOUR EMAIL ADDRESS', 'YOUR EMAIL PASSWORD')
server.sendmail('SENDERS EMAIL',
                'RECIEVER'S EMAIL',
                'YOUR MESSAGE'
                )
