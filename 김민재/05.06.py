from collections import defaultdict
N = int(input())
answer = 0

for _ in range(N):
    words = input()
    if words == 'ENTER':
        dic = defaultdict(int)
        continue
    dic[words] += 1
    if dic[words] == 1:
        answer += 1
print(answer)