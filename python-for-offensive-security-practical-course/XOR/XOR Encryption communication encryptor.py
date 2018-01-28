# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import string # The random and string libraries are used to generate a random string with flexible criteria
import random



# Random Key Generator

#key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(1024))

#from kali:
key = 'FPDi[Of9n/%5(b8\-mi)LT?tG7+>XERFU3?/$)^,8oRDWA_U/ty4>+]8sI.Fj\;Bc!#hI?$|Pm2gkbz(5:e>;AwQ}^?{]TK>\R2Z.v{QPdGYG6+MAhxnN6prX,bg-foyg,q\;}VPtn0uVS{ZrgyHd2o$$}}^hN0k?W.hyp)CL&ZMs&}Aloe0:N9Fbf:g8j][~Fr1+l7u]7GD$A5\=OsOBMN4v/)6{^<}Uzt>L{tJZhN:H/.=WaXzfp{8aLS{v/-DkBDYW{[N&\Q/{0,k4uAwf)/l}MYMQ[-EE0(l%4.Jg?BE_Hk-O!d:174HMOc<o.+-%i,jk_Oszdb=Ucx{wbU^g/C=RS-\<%75;mWhD}v2T_%2LNi:;b4]Vq\#?<t%lrucYe;\Wda&/k;e#aT%Fly^O>w4H_25h#owcOr\ZYv]Wrn-!KDvbu\]PftbdxCOA>Jhc8I(tX&(]P|%QVa+qs}3MIy6in\V&aUv#;T.|sVZ5GMC?[!4kJdDRjwi3Pr#gEsH8!({-BsCEm9HQ#=mLzuNXYK>X_i+$K0Lx)tP,%UT:O!Z6^XOX}EqYsAvEC4-JxbO:-=}k{F\d+e;wt,9f>7V4q6IA4l3l6[(4kEzD#k78Su$j+,gI7r0y;[<a(54O\IQj|.TE<S:MWrMEs=5zzgW4Jx4mC/h?pRd6EMEklD/=wr0r0h%14d:%LN&#Z)oo[JAt)k:MN-H[y_69W[vqqe0.M1bsCm(_}vcXzkz59:Sn{quhVQRp_ZP3E3y$c\%JaPijf3xCX,:~D[%|359%3I(oy5!|Zn:Q-_YsYTn2p6M+Un[s\}uU=?%2K$Yf>\Zi+&^|z|4IU-rYc/T+~JsC&nDre0::Y!!Tv<}B<>e0__OH#:LeelQe^h2~gq|2;>Xt&D9vu3r3$;Wu#^sA$ZJ.PaUdBir0I$0#epTzQN#NBu\C_$M\VmO8Jc-an7Xe=C4X^e]h_zAce]=48DfX}?2M9kt7lN7s<uyI^\~tfZFW#l-%o8lkz\.es^$Sf=?O-q;J)]d'

# the for loop defines the key size, key size is 1 KB which if you remember in our TCP shell, it matches the TCP socket size :)
# the  "".join   will put the result for the random strings into a sequqnece and we finally will store it in a key variable 
# so all in all the for loop will generate a 1024 random string which are matching our criteria  and . join is used to gather these strings into a sequenece


print key
print '\n' + 'Key length = ' + str (  len(key) )



# After we generate the XOR key, you need to take into consideration the XOR encrytpion rule which says the key length must be greater or equal the msg/data
# which we will send over the tunnel.    len(key) >= len(message) 


message = 'huj ci w dupe'  # this is the message which we will encrypt before it's getting sent
print "Msg is " + message + '\n'



# here i defined a dedicated function called str_xor, we will pass two values to this fucntion, the first value is the message(s1) that we want to encrypt or decrypt, 
# and the second paramter is the xor key(s2). We were able to bind the encryption and the decryption phases in one function because the xor operation is exactly the
# same when we encrypt or decrpyt, the only difference is that when we encrypt we pass the message in clear text and when we want to decrypt we pass the encrypted message

def str_xor(s1, s2):
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])


# first we split the message and the xor key to a list of character pair in tuples format >>  for (c1,c2) in zip(s1,s2)

# next we will go through each tuple, and converting them to integer using (ord) function, once they converted into integers we can now 
# perform exclusive OR on them  >>  ord(c1) ^ ord(c2)

# then convert the result back to ASCII using (chr) function  >>  chr(ord(c1) ^ ord(c2))
# last step we will merge the resulting array of characters as a sequqnece string using >>>  "".join function 




#Here we do a quick test 

enc = str_xor(message, key)
print 'Encrypted messge is: ' + '\n' + enc + '\n' 


#dec = str_xor(enc, key)
#print 'Decrypted messge is: ' + '\n' + dec

#Make sure that the SAME Key is HARDCODED in the Server AND client, ohterwise you won't be able to decode your own messages!



