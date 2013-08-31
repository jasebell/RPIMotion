#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import urllib

def sendSMS(uname, pword, numbers, sender, message): 
	params = {'uname':uname, 'pword':pword, 'selectednums':numbers, 'message':message, 'from':sender} 
	f = urllib.urlopen('https://www.textlocal.co.uk/sendsmspost.php?' + urllib.urlencode(params)) 
	return (f.read(), f.code)

_username = "username@domain.com"
_password = "password"
_fromtel  = "4407900xxxxxx"
_totel    = "4407900xxxxxx"
_message  = "There's been movement detected in the house."

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
      sendSMS(_username, _password, _totel, _fromtel, _message)
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      print "  Ready"
      Previous_State=0
      
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  GPIO.cleanup()
