# 인사성 밝은 곰곰이
## 시간 초과 문제 발생하는 코드

n=int(input())

m=[]
cnt=0
c=0
for i in range(n):
    a=input()
    if a=='ENTER': 
        m=[]
    else:
        
        if len(m)==0:
            m.append(a)
            cnt+=1
        else:
            for j in m:
                if a==j: #똑같은 닉네임이 있다면?
                    break
                
                m.append(a)
                cnt+=1
print(cnt)