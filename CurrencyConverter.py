#cocubes exam code
def CurrencyConverter(code,amount):
    if(code==1):
        return 65*amount
    elif(code==2):
        return amount*96
    elif(code==3):
        return 67*amount
    elif(code==4):
        return 74*amount
    elif(code==5):
        return 11*amount
print(CurrencyConverter(2,500))

#output:48000
