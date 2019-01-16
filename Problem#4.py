# This problem was asked by Stripe
#
# Given an array of integers, find in linear time and constant space. In other words, find the lowest positive
# integer that doesnt exist in the array. The array can contain duplicate elements as welll as negative numbers
#
# For example: the input[3,4,-1, 1] should give 2. The input[1,2,0] should output 3.
#
# You can modify the input array in place

from __future__ import division

def find_min_positive(in_list):
    maxi = max(in_list)+2

    for i in range(1, maxi):
        if i not in in_list:
            print(i)
            break
        else:
            continue

length = int(input("How long is your list? "))
print("Populate your array: ")
inlist = []
for j in range(length):
    k = int(input())
    inlist.append(k)
print("For input array : "+str(inlist))
print("The minimum possible positive integer is: ")
find_min_positive(inlist)