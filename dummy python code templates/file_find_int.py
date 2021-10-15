import re

with open("input.txt","r") as fin:
	s=fin.read()
	number=re.findall("\D+",s)
fin.close
print(number)
