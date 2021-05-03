# email_bot

**THE GOOGLE WILL GIVE YOU A ERROR HOW TO FIX IT IS FIRST GO TO YOUR GMAIL THERE YOU WIL GET MAIL THAT SOMEONE IS TRYING TO SEND EMAIL FROM YOUR ACCOUNT TO TURN ON THIS THE LINE WHERE THE URL BAR IS THERE, THERE YOU FIND THREE DOTS CLICK ON IT AND THEN CLICK ON MANAGE YOU GOOGLE ACCOUNT ON THE LEFT SIDE PANEL CLICK ON SECURITY SCROLL DOWN A LITTLE AND THERE YOU WILL FIND LESS SECURE APP ACCESS THEN AT THE DOWN THERE IS TURN ON ACCESS CLICK ON THAT AND THEN TURN ON THE APP ACCESS AND IT IS DONE NOW YOU CAN SEND YOUR EMAILS WITH YOUR OWN MADE BOTS**

Now you need not write 100 of mails with your hand with just 8 lines of python you can make your Email Bot and it will be amazing!!
I have done it by using Pycharm which is an python code editor.
At the first I have imported smtplib which is already installed with python.
Then I have created a variable called server and entered the value as smtplib.SMTP('smtp.gmail.com', 587).
Then I have told the variable server that starttls() so I would write it as server.starttls().
Then again I have told the server that server.login('YOUR EMAIL ADDRESS', 'YOUR EMAIL ADDRESS PASSWORD').
Then you will write server.sendmail('SENDERS EMAIL ADDRESS',
                    'RECIEVER'S ADDRESS',
                    'AND YOUR MESSAGE'
                    )
WOOHOO now your email bot is ready!!                    
