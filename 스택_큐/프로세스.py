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
    result = [0] * len(priorities)
    idx_list = priorities
    
    for i in range(len(priorities)):
        if len(priorities) != len(result) : 
            max_value = max(priorities)
            max_idx = idx_list.index(max_value)
            priorities.pop(max_idx)
            idx_list[max_idx] = 0
            
            if max_value == max(priorities)
                if f_max_idx > max_idx:                
                    priorities.pop(max_idx)
                    priorities.append(max_value)

            temp = max(priorities)
            priorities.pop(max_idx)
            
            if max(priorities) == temp:
                a_temp = priorities.index(max(priorities))
                if max
                if a_temp > max_idx and max:
                    priorities.insert(max_idx, max(priorities))      
                    max_idx = a_temp
                    dense = True
                    while dense:
                        
                
                else:
                    result[max_idx] = i+1
                
            
        else:
            f_max_idx = priorities.index(max(priorities))    
            priorities.pop(f_max_idx)
            idx_list[f_max_idx] = 0
            result[f_max_idx] = i+1       
        
        
    return answer
        
    return answer
