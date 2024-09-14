'''
종이조각 소수 만듦
numbers = 숫자가 적힌 문자열
만들 수 있는 소수 return

'''




def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    
    def generate(chosen, used):
        if len(chosen) == r:
            result.append(chosen.copy())
            return 
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result
    
def prime(temp):
    
    if temp == 1 or temp == 0:
        return False
        
    for k in range(2, int(temp**(0.5))+1) :
        
        if temp % k == 0:
            return False
    
    return True
    
    
def solution(numbers):
    answer = 0
    prime_number = []
    temp = []
    for i in numbers:
        prime_number.append(i)
    
    for j in range(1, len(prime_number)+1):
        combi = permutation(prime_number,j)
        for s in combi:
            temp.append(int("".join(s)))
            
    
    temp =set(temp)
    print(temp)
    for a in temp:
        result = prime(a)
        
        if result:
            answer+=1
        
        
    
    return answer
