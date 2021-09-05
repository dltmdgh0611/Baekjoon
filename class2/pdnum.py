li = []
while(True):
    word = input()
    if word == '0': break
    li.append(word)

for i in li:
    f = []
    s = []
    if len(i)%2==0:
        middle = int(len(i)/2)
        f = i[:middle]
        s = i[middle:]
        if f == s[::-1]: print("yes")
        else : print("no")
    else:
        middle = int(len(i)/2)
        f = i[:middle]
        s = i[middle+1:]
        if f == s[::-1]: print("yes")
        else : print("no")
        



