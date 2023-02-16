#cocubes exam code
def SumOrProduct(a,b,c,op):
    if op=="+":
        return (-b//a)+(c//a)
    elif op=="*":
        return (b//a)-(c//a)
a=3
b=9
c=6
op="+"
print(SumOrProduct(a,b,c,op))

#output:-1
