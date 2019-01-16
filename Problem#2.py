# This problem was asked by Uber
#
# Given an array of integers, return a new array such that each element at index i is the product
# of all numbers in the original array except one at index i
#
# For example, if our input was [1,2,3,4,5], the expected output would be  [120,60,40,30,24]. If the output was
# [3,2,1], the expected output would be [2,3,6]

inList1 = [1, 2, 3, 4, 5]
inList2 = [3, 2, 1]

def outCompute(input_list):
    outList = []         #  To store output multiples
    productList = []     #  To store the products to be multiplied
    a = 0
    for j in range(len(input_list)):
        product = 1
        #  loop to create a list without the current index
        for i in input_list:
            if i == input_list[a]:
                pass
            else:
                productList.append(i)
        #  loop to multiply factors in the current list
        for k in productList:
            product *= k
        outList.append(product)
        a += 1
        productList.clear()
    print(outList)

print(" First array")
outCompute(inList1)
print(" Second array")
outCompute(inList2)
