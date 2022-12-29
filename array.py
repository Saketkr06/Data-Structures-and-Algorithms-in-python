from array import *
arr1=array('i',[1,2,3,4,5])
arr2=array('d',[1.2,1.4,1.5])


arr1.insert(4,7)
print(arr1)
arr1.insert(0,0)
print(arr1)


def traversalArray(arra):
    for i in arra:
        print(i)
print(traversalArray(arr1))

def accessElement(array,index):
    if index > len(array):
        print('Thre is not any element in index')

    else:
        print(array[index])

accessElement(arr1,1)

def searchInArray(array,value):
    for i in array:
        if i==value:
            return array.index(value)

    return "The element doesnot exist in this array"

print(searchInArray(arr1,7))

arr1.remove(1)
print(arr1)
from array import *
my_array=array('i',[1,2,3,4,5]) #creating an array

for i in my_array: #traversing
    print(i)

#accesiing elements through indexes

print(my_array[0])

#appending element in array..as it add ends of array
my_array.append(6)
print((my_array))

#inserting value in array
my_array.insert(0,11)
print(my_array)

#extend of array by more than one value
my_array1=array('i',[10,12,13])
my_array.extend(my_array1)
print(my_array)

#add items from list to array

temp_list=[20,21,22]
my_array.fromlist(temp_list)
print(my_array)

#remove
my_array.remove(10)
print(my_array)

my_array.pop()
print(my_array)

print(my_array.index(21))
my_array.reverse()
print(my_array)

my_array.buffer_info()
print(my_array)

print(my_array.count(11))

#find missing no between 1 and 100

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(50*101)
print(50*101-sum(mylist))#sum of element
def findMissing(list,n):
    sum1=100*101/2
    sum2=sum(list)
    return sum1-sum2
print(findMissing(mylist,100))

#Write a program to find all pairs of integers whose sum is equal to a given no:
#pairs to be distnict
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i]+nums[j]==target:
                print(i,j)


mylis=[1,2,3,2,3,4,5,6]
print(findPairs(mylis,6))

