from random import choice

def first_lower(s):
   if len(s) == 0:
      return s
   else:
      return s[0].lower() + s[1:]

words = list()

academic = open('words.txt').read()
poems = open('poems.txt').read()

for line in academic.splitlines():
    words.append(first_lower(line))
for line in poems.splitlines():
    words.append(line)

print(choice(words))
for i in range(20):
    print (choice(words))
