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
                
                print(m)
                m.append(a)
                cnt+=1


print(cnt)