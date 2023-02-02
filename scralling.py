import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.iitb.ac.in/en/about-iit-bombay/contact-us'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
address = soup.find('div',{'class':'contact-details'})
if address==None:
    print('------')
else:
    x = address.find('p').text
    print(x)
    x = re.sub('\t','\n',x)
    print(x)
