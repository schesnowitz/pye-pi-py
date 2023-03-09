import re
import nltk
from nltk import stopwords
english_stopwords = stopwords.words("english")


with open("miracle.txt", "r", encoding='utf8', errors='ignore') as file:
    book = file.read()

pattern = re.compile("[A-za-z]+")
findings = re.findall(pattern, book.lower())
print(len(findings))

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1


d_as_list = [(value, key) for (key, value) in d.items()]
d_as_list = sorted(d_as_list, reverse=True)
print(d_as_list[:10])