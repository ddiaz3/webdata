import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#http://py4e-data.dr-chuck.net/known_by_Alva.html

url = input('Enter - ')
coun=input('Enter your count:')
pos=input('Enter your position:')
print(url)

for i in range(int(coun)):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,"html.parser")
	tags = soup('a')
	url = tags[int(pos)-1].get('href',None)
print (url)
