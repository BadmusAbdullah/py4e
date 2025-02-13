import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


url = input("Enter the url: ")

xlm_data = urllib.request.urlopen(url).read()


tree = ET.fromstring(xlm_data)
counts = tree.findall(".//count")

total = 0

for count in counts:
    num = int(count.text)
    total += num
print("Sum:", total)
