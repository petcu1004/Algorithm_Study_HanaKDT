# 인사성 밝은 곰곰이
## 시간 초과 문제를 집합으로 해결함.
import sys

input = sys.stdin.readline

n=int(input())
s=set() #애초에 중복 허용 X
cnt=0
input() #ENTER

for i in range(n-1):
    user=input().strip()#공백 없게 넣을 수 있도록 strip()함수 사용
    if user=="ENTER":
        cnt+=len(s)
        s.clear()
    else:
        s.add(user)
cnt+=len(s)

print(cnt)