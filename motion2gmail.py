#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import smtplib

def sendEmail():
  username = "xxxxxx"
  password = "xxxxxx"
  FROM = "jasebell@gmail.com"
  TO = ["jasebell@gmail.com"]
  SUBJECT = "Testing sending using gmail"
  TEXT = "Motion was detected from the Raspberry Pi"

  message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
  try:
    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(FROM, TO, message)
    server.close()
    print 'successfully sent the mail'
  except:
    print "failed to send mail"

GPIO.setmode(GPIO.BCM)

GPIO_PIR = 7
print "PIR Module Test (CTRL-C to exit)"

GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

try:

  print "Waiting for PIR to settle ..."

  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Ready"     
    
  while True :
   
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==1 and Previous_State==0:
      print "  Motion detected!"
      sendEmail()
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      print "  Ready"
      Previous_State=0
      
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  GPIO.cleanup()
