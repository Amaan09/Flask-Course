import re
import fileinput

print('Names: ')

pattern = re.compile("^[A-Z][a-z]+\s[A-Z][a-z]+$")

for line in fileinput.input('data.txt'):
    for match in re.finditer(pattern, line):
        print(match.group())

print()
print('Addresses: ')

pattern = re.compile("\d+\s+\S+\s+\D+\d+")

for line in fileinput.input('data.txt'):
    for match in re.finditer(pattern, line):
        print(match.group())

print()
print('Mobile Numbers: ')

pattern = re.compile("(\d{3})-\d{3}-\d{4}")

for line in fileinput.input('data.txt'):
    for match in re.finditer(pattern, line):
        print(match.group())

with open ('data.txt', 'r' ) as f:
    content = f.read()
    content_new = re.sub('Dave', 'John', content)
    # ----------------------------IMP----------------------------------------
    # printing the file content after replacing Dave with John
    # Please compare the console output against data.txt to check if it's working
    print(content_new)