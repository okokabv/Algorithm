'''
논문 n편 중 h번 이상 인용 h편 이상, 나머지 h편 이하 인용 -> h최대값이 H-Index
citations = 인용 횟수 배열
return = H-Index 
'''

# 단순 정렬



# Binary Search

def solution(citations):
    citations.sort()
    start = 0
    n = len(citations)
    end = n
    
    while start < end:
        mid = (start + end) // 2
        
        if citations[mid] >= n- mid:
            end = mid 
        else:
            start = mid +1
            
    return n- start
