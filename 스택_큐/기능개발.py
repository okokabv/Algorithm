'''
진도 100% 일때만 서비스에 반영

개발 속도 다름 
배포는 앞에있는 기능이 배포될 때 뒤에 기능이 함께 배포됨
배포는 하루에 한번

작업의 진도 정수 배열 progresses
작업의 개발 속도 정수 배열 speeds
개발 속도 = 하루에 몇 퍼센트 속도

각 배포마다 몇개의 기능 return

앞에 먼저니까, 큐 이용
'''
# for문을 한개로 줄이고, 큐니까 pop을 이용하게 바꾸면 좋을 듯
def solution(progresses, speeds):
    answer = []
    end = 100
    cost_day = []
    for idx, v in enumerate(progresses):
        rest = end - v
        if rest % speeds[idx] == 0:
            cost_day.append(rest // speeds[idx])
        else: 
            cost_day.append(rest // speeds[idx] + 1)
    day = 0
    cnt = -1
    for idx, d in enumerate(cost_day):
        
        if day >= cost_day[idx]:
            answer[cnt]+=1
            
        else:
            day = cost_day[idx]
            answer.append(1)
            cnt +=1
    
    return answer
