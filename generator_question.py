def cube_generator(n):
    for i in range(1,n + 1):

        yield i ** 3

n = int(input('input number: '))


cubes = cube_generator(n)


print("cube of number from 1 to",n)


for num in cubes:
    print(num)




# Write a Python program to implement a generator that generates random numbers within a given range.







