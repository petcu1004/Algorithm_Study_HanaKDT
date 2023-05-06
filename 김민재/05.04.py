def solution(s):
    s = s.split()
    s = list(map(int, s))
    s.sort()
    answer = str(s[0]) + ' ' + str(s[-1])
    return answer