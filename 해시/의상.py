'''
코디 조합 개수 확인
종류별로 1개씩, 혹은 딱 1가지만 착용도 가능
최소 한개는 입음.
입력 clothes = [["의상이름", "종류"]]

'''
#식: (같은 i종류 옷 개수 + 1) * (같은 i종류 옷 개수 + 1 ) -1 
def solution(clothes):
    dic = {}
    for idx, i in enumerate(clothes):        
        if i[1] in dic:
            dic[i[1]].append(i[0]) # 이미 키 값이 저장되어 있으면 값 추가
        else:
            dic[i[1]] = [i[0]] # 키값 없으면 새로 키값 추가 후 값 추가
    temp = 1
    for i in dic.values():
        temp = (len(i)+1)*temp # 코디 개수 확인 식
    
    answer = temp-1 # 코디 개수 확인 식
    
    return answer
