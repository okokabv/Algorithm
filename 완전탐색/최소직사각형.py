'''
명함을 모두 명함 지갑에 수납
sizes = [가로길이, 세로 길이]
명함을 눕혀서 수납 가능
지갑의 크기 = 가로 x 세로

return = 지갑 크기


큰값, 작은 값 으로 정렬하고,
최대값 최대값 뽑아서 크기 구하기


'''

def solution(sizes):
    answer = 0
    temp = []
    temp2 = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        
        temp.append(sizes[i][0])
        temp2.append(sizes[i][1])
    
    
    answer = max(temp) * max(temp2)
    
    
    return answer
