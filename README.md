###String-Methods......


# capitalize()
name  = "i am developer frome tamilnadu"
a = name.capitalize()
print('capitalize--------',a)

# casefold()
name = "I AM Dveloper From Tamilnadu"
b = name.casefold()
print('casefold----------------',b)

# center()
name = "kutt y seenu"
c = name.center(30,"*")
print('center--------',len(c),c)

# count()
name  = "i am developer frome tamilnadu"
d  = name.count("arikrishnan")
print(d) 

# encode()
name  = "i am developer "
e = name.encode()
print(e)

# endswith()
name  = "i am developer."
f = name.endswith(".")
print(f)

# expandtabs()
name= 'i/am/ari/krishnan '
g=name.expandtabs(3)
print(g)

# find()
name  = "i am developer frome tamilnadu"
h=name.find("frome")
print(h)

# format()
p=40
c="chennai"
letters = "for only+ {price} rupees from {city}"
print(letters.format(price = p,city=c))

# index()
name  = "i am developer frome tamilnadu"
i = name.index("tamilnadu")
print('Index-------',i)

# isalnum()
name = "python37"
j = name.isalnum()
print('isalnum-------',j)

# isalpha()
name = "pythonYYY"
k = name.isalpha()
print(k)

# isascii()
name = "python251376"
l = name.isascii()
print(l)

# isdecimal()
numbers = "123456789"
m = numbers.isdecimal()
print(m)

# isdigit()
numbers = "555555"
n = numbers.isdigit()
print(n)

# isidentifier()
name  = "hello"
o = name.isidentifier()
print(o)

# islower()
name = "hello"
p = name.islower()
print(p)

# isnumeric()
numbers = "12345678"
q = numbers.isnumeric()
print(q)

# isprintable()
word = "Hai! Are you #1?"
s = word.isprintable()
print(s)

# isspace()
txt = " "
t = txt.isspace()
print(t)

# istitle()
words = "Hai, And Wellcom To My World!"
u = words.istitle()
print(u)

# isupper()
txt = "all is well!"
v = txt.isupper()
print(v)

# join()
Tuple = ("apple", "orang","banana")
w = "#". join(Tuple)
print(w)

#ijust()
name = "banana"
y = name.ljust(20)
print(y,"is my favert fruit.")
