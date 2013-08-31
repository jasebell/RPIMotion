# Raspberry Pi Motion Detection.

#### What you'll need.

[Raspberry Pi Computer](http://www.amazon.co.uk/gp/product/B009SMWSQA/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B009SMWSQA&linkCode=as2&tag=jasonbelljava-21)

[Passive Infrared Motion Sensor](http://www.amazon.co.uk/gp/product/B008AESDSY/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B008AESDSY&linkCode=as2&tag=jasonbelljava-21) (You only need the one but I order five at a time)

[Solderless Breadboard](http://www.amazon.co.uk/gp/product/B0040Z1ERO/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B0040Z1ERO&linkCode=as2&tag=jasonbelljava-21)

And you'll also need some wires to connect it all together. To see what goes where have a look at my blog post [Raspberry Pi PIR Motion Detection](http://dataissexy.wordpress.com/2013/06/29/raspberry-pi-pir-motion-detection-and-alerting-to-sms-raspberrypi-sms-sensors/)

##motion2sms.py

This Python script detects motion from the PIR and sends an SMS text message via the TextLocal service (in the UK) using their HTTP based API. 

## motion2gmail.py

Based on the same concept as the SMS motion detection this will send an email to your Gmail account.  You need to set the username, password in the sendEmail() method. Also be careful not to send too many emails out from your Pi, you don't want to upset Google. 

 