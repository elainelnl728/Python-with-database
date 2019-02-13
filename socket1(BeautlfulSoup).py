from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
#numbers = []
#spans = soup('span')
#for span in spans:
    # Look at the parts of a tag
 #   numbers.append(int(span.string))
#print sum(numbers)

tags = soup('span')

spans = [int(tag.contents[0]) for tag in tags]
summation = sum(spans)
print (summation)