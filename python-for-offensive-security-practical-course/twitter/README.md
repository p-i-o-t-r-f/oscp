Kali : Tweets Grabber

Grab txt tweets from Tim Ferris twitter account


beautiful3

provide twitter account and grab tweet


Client -TCP Reverse Shell twitter.py

like below:

##############################################

Exercise for russia malw: 
#Case study – Russian Malware
#https://www2.fireeye.com/APT29-HAMMERTOSS-WEB-2015-RPT.html
#https://www.fireeye.com/blog/threat-research/2015/07/hammertoss_stealthy.html

Kali: Server- TCP Reverse shell.py


Target Win: Client -TCP Reverse Shell twitter.py


1. Create a new twitter account for testing purposes.  

2. Tweet your kali IP address and a port number of your choice.   -> use no ip on the ITG phone connected to laptop, install virtualbox Kali machine, with no ip

3. From the Windows (Target) machine retrieve the HTML of https://twitter.com/<YourAccount> and parse the tweet which you have just created.

beautiful 3.py

4. Use our previous persistent reverse TCP shell (which we created in module 2) and instead of hardcoding the IP address of the Kali, make it dynamically changing based on the latest tweet.

on Target WIN: Client -TCP Reverse Shell twitter.py  

5. Verify that the connection to the kali is successful.


6. Restart the windows PC and make sure that all other features like persistency, number of connections attempts are working as expected.

so then used Client - TCP reverse shell twitter.py and created by py2exe exe file: twitter.exe
and then create another file persistance

twitter persistance.py