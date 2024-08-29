'''
많이 재생된 노래 2개씩 모아 베스트 앨범
고유번호 구분

많이 재생된 장르먼저 수록
장르 내에 많이 재생된 노래 먼저
재생 같으면 고유 번호 낮은 노래 먼저

장르 배열 genres
재생 횟수 배열 plays
'''
def solution(genres, plays):
    answer = []
    dic = {}
    for idx, i in enumerate(genres):        
        if i in dic:
            dic[i].update({idx:plays[idx],'total':dic[i]['total']+plays[idx]})
        else :
            dic[i] = {idx:plays[idx]}
            dic[i].update({'total':plays[idx]})
        
    dic = sorted(dic.items(), key= lambda item: item[1]['total'], reverse=True)
    
    for g,s in dic:
        s['total'] = 0
        s = sorted(s.items(), key= lambda item: item[1], reverse =True)
        
        if len(s) <=2 :
            answer.append(s[0][0])
        else:
            answer.append(s[0][0])
            answer.append(s[1][0])
    
    return answer
