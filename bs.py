# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl


# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ")
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup("a")
# for tag in tags:
#     print(tag.get("href", None))

import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://py4e-data.dr-chuck.net/comments_1985460.html"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("span", class_="comments")
total = 0

for tag in tags:
    num = int(tag.text)
    total += num
print("Sum:", total)
