'''
운영체제 프로세스 관리 실행
1. 실행 대기 큐에서 프로세스 하나 꺼냄
2. 큐에 우선순위가 더 높은 큐 있으면 방금 꺼낸거 다시 넣음
3. 2번 경우 아니면 꺼낸 프로세스 실행
3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 종료

priorities = 우선순위 담긴 배열
location = 몇번째로 실행되는지 알고싶은 프로세스 위치 (0번부터 시작)
'''

def solution(priorities, location):
    answer = 0
    index_p = []
    for idx, p in enumerate(priorities):
        index_p.append([idx,p])
    
    sorted_p = sorted(priorities, reverse=True)
    
    while index_p:
        check = index_p.pop(0)
        
        if check[1] == sorted_p[0]:
            sorted_p.pop(0)
            answer +=1
            
            if check[0] ==location:
                return answer
        
        else:
            index_p.append(check)
    
    return answer
        
    return answer
