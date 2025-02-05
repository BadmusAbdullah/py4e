import re

print("Regular Expressions")
# hand = open("mbox-short.txt")

hand = open("regex_sum_1985458.txt")
for line in hand:
    nums = re.findall("[0-9]+", hand.read())
    int_list = []
    for num in nums:
        int_list.append(int(num))
    print(sum(int_list))

# for line in hand:
#     line = line.rstrip()
#     email = re.findall("\S+@\S+", line)
#     print(email)
# if line.find("From:") >= 0:
# if re.search("From:", line):
#     print(line)
