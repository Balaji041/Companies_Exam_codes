#Cocubes Exam code

def RelativeTime(di,d1,s1,d2,s2):
    if di==0:
        time1=d1//s1
        time2=d2//s2
        return time1+time2
    elif d1==1:
        time1=d1//s1
        time2=d2//s2
        return time1-time2
di=0
d1=30
s1=5
d2=20
s2=10
print(RelativeTime(di,d1,s1,d2,s2))
