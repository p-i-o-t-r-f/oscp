import urllib
from BeautifulSoup import BeautifulSoup
#url = "https://www.hackthissite.org"
#url ="https://twitter.com/arkadiuszbeer"
#url ="https://twitter.com/tferriss"
url = raw_input("Enter the URL ")
ht= urllib.urlopen(url)
html_page = ht.read()
b_object = BeautifulSoup(html_page)



data2 = b_object.body.find('div',attrs={'class' : 'js-tweet-text-container'})

print data2.text

#for data3 in b_object.body.find('div',attrs={'class' : 'js-tweet-text-container'}):
#print data2
# print data3.text
