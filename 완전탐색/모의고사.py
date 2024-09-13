'''
가장 많이 맞춘 사람
answers = 정답
return = 가장 많이 문제 맞춘 사람 번호

1번: 1,2,3,4,5, ....
2번: 2,1,2,3,2,4,2,5, ...
3번: 3,3,1,1,2,2,4,4,5,5, ...

'''

def solution(answers):
    answer = []
    one = [1,2,3,4,5] * 2000 
    two = [2,1,2,3,2,4,2,5] * 2000
    three = [3,3,1,1,2,2,4,4,5,5] * 2000
    
    one_cnt = 0
    two_cnt = 0
    three_cnt = 0
    
    for i in range(len(answers)):
        
        if one[i] == answers[i]:
            one_cnt +=1
        if two[i] == answers[i]:
            two_cnt +=1
        if three[i] == answers[i]:
            three_cnt +=1
            
    a_value = [one_cnt, two_cnt, three_cnt]
    max_value = max(a_value)
    for a in range(len(a_value)):
        if max_value == a_value[a]:
            answer.append(a+1)
            
    return answer
