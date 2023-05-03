#최댓값과 최솟값

def solution(s):
    answer = ''
    a=[]
    a=list(map(int,s.split(" ")))

    answer+=str(min(a))
    answer+=' '
    answer+=str(max(a))

    return answer