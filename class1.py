# a = input().split()
# print(int(a[0]) + int(a[1]))

# a = input().split()
# print(int(a[0]) - int(a[1]))

# a = input().split()
# print(int(a[0]) / int(a[1]))

# a = input().split()
# print(len(a))


# import string
# d = dict.fromkeys(string.ascii_uppercase, 0)
# word = list(input())

# for i in word:
#     if ord(i) > 96: i = chr(ord(i)-32)
#     d[i] = d[i] + 1
    
# result = [k for k,v in d.items() if max(d.values()) == v]
# if len(result) > 1: print("?")
# else: print(''.join(result))

# a = input().split(" ")
# if int(a[0]) == int(a[1]) : print("==")
# elif int(a[0]) < int(a[1]) : print("<")
# else : print(">")

# len = int(input())
# a = list(map(int, input().split()))
# max = max(a)
# for c ,i in enumerate(a):
#     a[c] = i/max*100
# print(sum(a)/len)

# len = int(input())
# for i in range(len):
#     for k in range(i,len-1):
#         print(" ", end='')
#     for j in range(len-i-1,len):
#         print("*", end='')
#     print()

# a = list(map(int, input().split()))
# result = 0
# for i in a:
#     result = result + i*i
# print(result%10)

# li = []
# for i in range(9):
#     li.append(int(input()))
# di = {}
# for c, i in enumerate(li):
#     di[c+1] = i
# print(max(di.values())) max value
# print(max(di,key=di.get)) max value에 대한 key

num = 1
li = [0 for i in range(10)]
for i in range(3):
    num = num * int(input())
for j in [int(x) for x in str(num)]:
    li[j] = li[j]+1
for k in li:
    print(k)