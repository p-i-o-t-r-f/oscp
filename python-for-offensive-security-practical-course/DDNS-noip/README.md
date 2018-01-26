Kali : DDNS Aware Shell



no-ip aggent installing:

1. cd /usr/local/src/

2. wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz

3. tar xf noip-duc-linux.tar.gz

4. cd noip-2.1.9-1/

5. make install



Z <http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/> 

To Configure the Client

As root again (or with sudo) issue the below command:

• /usr/local/bin/noip2 -C (dash capital C, this will create the default config file)
You will then be prompted for your username and password for No-IP, as well as which hostnames you wish to update. Be careful, one of the questions is “Do you wish to update ALL hosts”. If answered incorrectly this could effect hostnames in your account that are pointing at other locations.
Now the client is installed and configured, you just need to launch it. Simply issue this final command to launch the client in the background:

• /usr/local/bin/noip2
