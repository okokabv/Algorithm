
'''
hdd 한 번에 하나의 작업만 수행
디스크 컨트롤러 구현
-> 요청이 들어온 순서대로


jobs = [요청 시점, 소요시간]
요청시점+소요시간 = 작업시간 
return 작업 최소 평균시간 (소수점 버림)  // 사용


요청 시점 = idx
소요시간 = 값

'''



import heapq

def solution(jobs):
    answer = 0
    now = 0
    finish = 0
    start = -1
    heap = []
    
    while finish < len(jobs): # 입력값 다 돌면 끝
        for i in jobs:
            if start < i[0] <=now: # 시작지점, 현재 사이의 값이면 힙에 넣기
                heapq.heappush(heap, [i[1], i[0]])
                pass
        
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            finish +=1
        else: 
            now +=1
            
    answer = answer // len(jobs)
    return answer
