# number = (1,2,3,4,5,6,7,8,9)



# even = 0

# odd = 0


# for i in number:

#     if i % 2 == 0:

#         even += 1

#     else:

#         odd += 1


# print(even)
# print(odd)


# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')



# x,y = 0,1

# while y<50:
#     print(y)
#     x,y = y,x+y



# for i in range(1,51):

#     if i%3 == 0:
#         print('fizzz')
#         continue

#     elif i%5 == 0:
#         print('buzz')
#         continue

#     elif i%3==0 and i%5==0:

#         print('fizzbuzz')
#         continue


#     print(i)



# text = input('enter txt in lower case : ')


# lines = []


# for i in text:

   

#     lines.append(i.upper())



# for l in lines:

#     print(l,end='')
	

sample = input()

letters = 0

digits = 0

for i in  sample:

    if i.isdigit():

        digits += 1


    elif i.isalpha():

        letters += 1

    
    else:

        pass

      


print(letters)

print(digits)
    
























