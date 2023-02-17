#mitsogo exam code
from collections import deque
input1=[10,20,30,40,50]
input2=[20,30,40,50,10]
input3=5
counts = []
for i in range(input3):
    myarray = deque(input1)
    myarray.rotate(1)
    input1=list(myarray)
    c=0
    for j in range(input3):
        if input1[j]==input2[j]:
            c+=1
    counts.append(c)
print(max(counts))

#output:5
