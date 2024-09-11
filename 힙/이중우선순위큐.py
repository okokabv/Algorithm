'''
이중 우선순위 큐
I 숫자 = 큐에 주어진 숫자 삽입
D 1 = 큐에서 최댓값 삭제
D -1 = 큐에서 최소값 삭제

모든 연산 처리 후 큐가 비어있으면 
[0,0]
비어있지 않으면 [최대값, 최소값]

힙을 2개 만들어서, 최대힙, 최소힙 만들고 최소값 최대값 빼면 되지 않을까
아니면 힙 1개로 반대로 빼면 되려나
일딴 힙 조금만 사용하고 나머지 만듦 -> 수정 필요

'''


import heapq

def solution(operations):
    answer = []
    heap = []
    for i in operations:
        
        if "I" in i:
            heapq.heappush(heap, int(i.split()[1]))
        elif len(heap) > 0 and "D -1" in i:
            min_value= min(heap)
            idx = heap.index(min_value)
            heap.pop(idx)
        elif len(heap) > 0 and "D 1" in i:
            max_value = max(heap)
            idx = heap.index(max_value)
            heap.pop(idx)
        
    if len(heap) < 1:
        answer = [0,0]
    else: 
        answer.append(max(heap))
        answer.append(min(heap))
        
    return answer
