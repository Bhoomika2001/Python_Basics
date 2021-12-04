#Generate Random Numbers in Python

import random
print(random.random())
print(random.randrange(0,10))
print(random.uniform(0,10))

#1 to 10

x = random.uniform(1,10)
print(x)

#Make a program that creates a random number and stores it into x.

x = random.random()
print(x)


#Make a program that prints 3 random numbers.

import random
randomlist = []
for i in range(0,3):
 n = random.randint(1,30)
 randomlist.append(n)
print(randomlist)


#Create a program that generates 100 random numbers and find the frequency of each number.

