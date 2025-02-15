import json, ssl
import urllib.request, urllib.parse, urllib.error


url = input("Enter url: ")
print("Retrieving", url)

response = urllib.request.urlopen(url)
data = response.read().decode()

print("Retrieved", len(data), "characters")

try:
    json_data = json.loads(data)
except:
    print("Error parsing JSON")
    quit()

sum = 0
count_list = json_data.get("comments", [])

print(count_list)

for comment in count_list:
    sum += int(comment.get("count", 0))

print("Sum:", sum)
