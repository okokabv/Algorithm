'''
갈색 격자 수 = brown
노란색 격자 수 = yellow

카펫의 가로, 세로 크기를 return
카펫의 가로 길이 >= 세로 길이

1 =  3
2 = 4
3  = 5
4 = 6

1 x 1 = 3, 3  -> (1x2)+(1x2)+4 필요한 타일 수: 8개
2 x 1 = 4, 3 -> 10개   (2x2)+(1x2)+4 =10  
3 x 1 = 5, 3 -> 12개 (3x2) + (1x2) +4 = 12

2 x 2 = 4, 4
3 x 2 = 5, 4

6 x 4 = 8, 6 -> (6x2)+(4x2)+4 = 24 

ex) 

b = 15, y =20 

y x 1 <= y
(y-1) x 1 <= y
(y-1) x 2 <= y



5 x 4 = 7, 6 -> (5x2)+(4x2)+4 = 22 > b  안됨
6 x 3 = 8, 5 -> (6x2)+(3x2)+4 = 22 > b  
7 x 2 = 9, 4 -> (7x2)+(2x2)+4 = 22 > b
5 x 3 = 7, 5 -> (5x2)+(3x2)+4 = 20 > b


너무 느림, 시간 복잡도 개선 해야 할듯

'''



def brown_used(x,y):
    return (x*2)+(y*2)+4

def yellow_used(y_num, b_num):
    temp = [0,0]
    for i in range(y_num,0, -1):
        for j in range(1, (y_num//i)+1):
            if i*j <=y_num and i>=j:
                if brown_used(i, j) > b_num:
                    break
                if (temp[0] * temp[1]) < (i*j) :
                    temp = [i,j]
                    
    mn = temp
    return mn
        
def solution(brown, yellow):
    answer = []
    array = yellow_used(yellow, brown)
    answer = [array[0]+2, array[1]+2]
    
    
    return answer



