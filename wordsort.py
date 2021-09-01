# 중복 제거 set
# 정렬 sorted
#for i in range(len(words)):
#     for j in range(i, len(words)):
#         if len(words[i]) > len(words[j]): #string의 length로 정렬
#             tmp = words[i]
#             words[i] = words[j]
#             words[j] = tmp
#         elif len(words[i]) == len(words[j]): # 같을 경우 알파벳순
#             sortli = [words[i], words[j]]
#             sortli.sort()
#             if sortli[0] == words[j]:
#                 tmp = words[i]
#                 words[i] = words[j]
#                 words[j] = tmp

length = input()

words = []

for i in range(int(length)):
    word = str(input())
    word_length = len(word)
    words.append((word, word_length))

words = list(set(words))

words.sort(key=lambda word: (word[1],word[0]))

for word in words:
    print(word[0])