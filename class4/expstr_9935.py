str = input()
exp = list(input())
le = len(exp)
answer = []
for st in str:
    answer.append(st)
    if answer[-le:]==exp:
        answer[-le:] = []

if len(answer) == 0:
    print('FRULA')
else:
    print("".join(answer))