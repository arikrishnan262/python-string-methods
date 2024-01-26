#capitalize()
name  = "i am arikrishnan frome tamilnadu"
a = name.capitalize()
print('capitalize--------',a)

# casefold()
name = "I AM Arikrishnan From Tamilnadu"
b = name.casefold()
print('casefold----------------',b)

# center()
name = "kutt y seenu"
c = name.center(30,"*")
print('center--------',len(c),c)

# count()
name  = "i am arikrishnan frome tamilnadu"
d  = name.count("arikrishnan")
print(d) 

# encode()
name  = "i am arikrishnan "
e = name.encode()
print(e)

# endswith()
name  = "i am arikrishnan."
f = name.endswith(".")
print(f)

# expandtabs()
name= 'i/am/ari/krishnan '
g=name.expandtabs(3)
print(g)

# find()
name  = "i am arikrishnan frome tamilnadu"
h=name.find("frome")
print(h)

# format()
p=40
c="chennai"
letters = "for only+ {price} rupees from {city}"
print(letters.format(price = p,city=c))

# index()
name  = "i am arikrishnan frome tamilnadu"
i = name.index("tamilnadu")
print('Index-------',i)

# isalnum()
name = "kuttyseenu37"
j = name.isalnum()
print('isalnum-------',j)

# isalpha()
name = "kuttyseenuY"
k = name.isalpha()
print(k)

# isascii()
name = "kuttyseenu251376"
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
name  = "kutty"
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
Tuple = ("kutty", "surya","vicky")
w = "#". join(Tuple)
print(w)

#ijust()
name = "banana"
y = name.ljust(20)
print(y,"is my favert fruit.")