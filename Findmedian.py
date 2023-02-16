#cocubes exam code
import statistics
def Findmedian(arr1,arr2):
    add=arr1+arr2
    add.sort()
    return statistics.median(add)
arr1=[2,3,5,7,8]
arr2=[3,3,7,9,10]
print(Findmedian(arr1,arr2))

#output:6
