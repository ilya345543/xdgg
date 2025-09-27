a = 3
b = 2.56
print(type(a+b),(a+b),type(a-b),(a-b),type(a*b),(a*b),type(a/b),(a/b),)

pi = 3.14159
r = 5
s = pi*r**2
print(round(s,2))

text = ' Helo, Python! '
text = text.strip()
print(text)
text = ' Helo, Python! '
text = text.replace('!','?')
print(text)
text = ' Helo, Python! '
text = text.upper()
print(text)

num = [7, 2, 5]
num.append(4)
num.insert(2, 10)
num.extend([1, 1, 1])
num.remove(7)
pop = num.pop(-1)
num.sort()
num.reverse()
cnt = num.count(2)
ind = num.index(1)
n2 = num.copy()
n3= num[::]
num = num.clear()
print(num, n2, n3)

t = (1, 2, 3)
try:
     t[1] = 100
except:
     print('неизменяемый тип')

t1 = (4, 5)
t = (1,2,3)
t2 = t + t1
cnt = t2.count(3)
i = t.index(2)
print(t, t2, cnt, i)

values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(len(unique_values))
other = {2, 4, 5}
print(unique_values & other, unique_values | other, unique_values - other, other - unique_values)

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores['Bob'] = 95
print(scores)
scr = scores.get('Dave')
print(scr, scores.get('Bob'))
del scores['Alice']
print(scores, len(scores), scores.keys(), scores.values())

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores['Bob'] = 95
print(scores)
scr = scores.get('Dave')
print(scr, scores.get('Bob'))
del scores['Alice']
print(scores, len(scores), scores.keys(), scores.values())

text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text=text.strip().lower()
# print(text)
text =text.replace('!','.')
# print(text)
a = text.split('.')
for i in range(len(a)):
    a[i] = a[i].strip()
    if a[i]=='': a.remove(a[i])
print(a)
first = a[0].split()
print(first)
print(text.count('python'))
start = a[0].startswith("python")
end = a[0].endswith("language")
print(start, end)
print(len(text), text.count('a'), text.find("data"))
words = text.replace('.','').replace(',','').split()
print(words)
newText = ''
for i in words:
    newText += i + '-'
newText=newText[:-1]
d = {}
for i in newText.split('-'):
    if i not in d:
        d[i] = newText.count(i)
print(d)

def clean(text):
    return text.replace('.','').replace(',','').replace('!','').replace('?','').lower().strip()
print(clean('   Hello, World,      '))