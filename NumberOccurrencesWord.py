#cocubes exam code

def NumberOccurrencesWord(st,word):
    string=st.split()
    count=0
    for i in range(len(string)):
        if word==string[i]:
            count=count+1
    return count
st="tyiou abcd tyiou ijk! tyiou abcd tyiou acv tyiou"
word="tyiou"
print(NumberOccurrencesWord(st,word))
