

# String methods


# 1) captialize 


txt = 'hello my name is prashant '

print(txt.capitalize())

# in this methods it returns the string where the first character is upper and rest of the character is in lower case 


a = 'python IS FUN'

print(a.capitalize())


b = '35 is My AGE'

print(b.capitalize())


# 2) casefold

z = 'HELLO BOY'

print(z.casefold())

# it return all the character in lower case


# 3) center 

y = 'prashant'

print(y.center(20,'*'))
print(y.center(30,'&'))

#  it will return the centre align the string 
# syntax string.center(length,character)


# 4) count

# it will count the values entered in the string 


t = 'prashantkardile deeilp kardile'

print(t.count('a',0,8))
print(t.count('p'))


# 5) encode

# it will encode the string using utf-8


f = 'my name is prashant'

print(f.encode())

# 6) endswith

# methods retrun boolean value 

g = 'prashant'

print(g.endswith('nt'))
print(g.endswith('p'))
print(g.endswith('r',0,2))


# 7) format


u = 'my name is {name:} and my age is {age:e}'

print(u.format(name='prashant',age=22))
print(u.format(name='shubham',age=21))


# 8) find

# syntax

# string.find(value,start,end)


e = 'my name is prashant'

print(e.find('prashant'))

# 9) index 

#  find and index both are same 



# 10) isalnum

#  returns true or false if the value is alpha numeric means a-z 0-9
# spaces and other symbols are not allowed 


w = '12company'
r = '0com*'

print(w.isalnum())
print(r.isalnum())

# 11) isalpha 

#  retruns true or false if all the character is are alphabet


f1 = 'prashant'
g1 = '2000prashant'


print(f1.isalpha())

print(g1.isalpha())


# 12) isdecimal

# return true if all the character are in decimal values 

t = '66.66'
t1 = '81'

print(t.isdecimal())
print(t1.isdecimal())



# 13) isdigit

# returns true if all the character are digits otherwise false

i = '12.2'
i1 = '123'

print(i.isdigit())
print(i1.isdigit())



 















