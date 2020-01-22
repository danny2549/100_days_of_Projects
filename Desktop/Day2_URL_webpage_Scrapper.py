#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificat errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# In[ ]:


url = input('Enter -')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

