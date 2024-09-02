'''
가격이 떨어지지 않은 기간은 몇 초인지 return

prices= 초 단위 주식가격

'''


def solution(prices):
    answer = []
    idx_list = []
    
    for i in range(len(prices)):
        answer.append(0)
        for j in range(i+1,len(prices)):
            
            if prices[i] <= prices[j]:
                answer[i] +=1
                continue
            
            else: 
                answer[i] +=1
                break
            
    return answer
