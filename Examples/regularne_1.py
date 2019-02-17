import re

with open('C:\\Users\\kurs\\Desktop\\input.txt', 'r') as f:
    znaki = f.read()

print(re.findall(r'\b\d\d\-\d{3}\b', znaki)),
print(re.findall(r'[\w\-+]+@[\w\-.]{4}', znaki)),
print(re.findall(r'\b\d{1,2}\s[A-Z][a-z]{2}\s\d{4}\b', znaki)),

