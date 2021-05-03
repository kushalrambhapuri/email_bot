import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('kushal.rambhapuri@gmail.com', 'Kushal@0711')
server.sendmail('kushal.rambhapuri@gmail.com',
                'kushal.rambhapuri@gmail.com',
                'Hi How are you?'
                )
