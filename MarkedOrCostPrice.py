#cocubes exam codes

def MarkedOrCostPrice(n,percent,sp):
    if n==1:
        return(sp*100)//(100-percent)
    elif n==2:
        return(sp*100)//(100+percent)
n=1
percent=20
sp=200
print(MarkedOrCostPrice(n,percent,sp))
"""
Output:250
"""
