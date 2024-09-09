'''
스코빌 지수 K 이상으로 새로 만들고 싶음

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

스코빌 지수가 K이상이 될떄까지 섞음

scoville = 스코빌 지수를 담은 배열
K이상으로 만들때 음식을 섞어야하는 최수 횟수 return 
모든 음식을 K이상으로 다 만들 수 없으면 -1 return


힙 = 완전 이진 트리
-> 이진 트리 탐색 -> 나누기 2
#힙을 직접 구현하면 느려서 시간초과에 걸림

'''


import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    
    while scoville and scoville[0] < K:
        if 1>=len(scoville):
            return -1
        
        else:
            sco_one = heapq.heappop(scoville)
            sco_two = heapq.heappop(scoville)
            sco_mix = sco_one+ (sco_two * 2)
            answer +=1    
            heapq.heappush(scoville, sco_mix)
                       
    return answer

