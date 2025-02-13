import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Dayna.html"

repeat = 7

position = 18

print("Starting URL: ", url)

for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    links = soup.find_all("a")

    if len(links) < position:
        print("Not enough links on the page!")
        break
    url = links[position - 1].get("href")
    name = links[position - 1].text
    print(f"Step {i+1}: Following link {url}, found name {name}")


print("Last name in sequence:", name)
