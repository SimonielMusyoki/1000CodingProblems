# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#Problem was asked by Google
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

from itertools import permutations
numlist = []
number = int(input("How many numbers do you want the list to have? "))
for i in range(number):
    m = int(input("Populate the list: "))
    numlist.append(m)
expectedNumber = int(input("Enter the sum to be checked: "))
sumList = []
perm = permutations(numlist,2)
for i in perm:
    j = list(i)
    a, b= j
    if a + b == expectedNumber:
        sumList.append(j)
if len(sumList)==0:
    print("No permutations found! ")
else:
    print("Permutations found! ")
    print("The following permutations add upto %s :"%(expectedNumber))
    for k in sumList:
        print(k)
