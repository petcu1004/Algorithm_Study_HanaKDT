def solution(n, words):
    answer = [0, 0]
    dic = dict()
    for i in range(len(words)):
        if i == 0:
            dic[words[i]] = 1
            continue
        if words[i-1][-1] != words[i][0] or words[i] in dic:
            answer = [i%n+1, i//n+1]
            break
        dic[words[i]] = 1
    return answer