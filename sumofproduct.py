#cocubes exam code


def sumofproduct(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+((n//i)*i)
    return sum
print(sumofproduct(4))
        
 #output:15
