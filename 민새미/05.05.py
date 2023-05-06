# 인사성 밝은 곰곰이
## 시간 초과 문제를 해시로 해결함.

n=int(input())

dic ={}
cnt=0

for _ in range(n):
    a=input()

    if a=="ENTER":
        for key, value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        if a not in dic: #중복되는 닉네임이 없을 경우
            dic[a]=1 #그에 맞는 value값을 1로 설정
    
for key, value in dic.items():
    if value==1:
        cnt+=1

print(cnt)
