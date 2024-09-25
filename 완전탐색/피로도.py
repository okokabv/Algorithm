'''
피로도 -> 0 이상의 정수
던전 탐험:
최소 필요 피로도: 최소한 가지고 있어야 하는 피로도
소모 피로도: 던전 탐험후 소모되는 피로도

dungeons = 던전별 최소 필요 피로도, 소모 피로도를 가진 2차원 배열 
k = 피로도
탐험 최대 던전 수 return


최소 필요도 - 소모 피로도 -> 남은 피로도
최대한 남은 피로도가 많게해서 던전 다 돌아야함

백트랙킹 -> 

ex) 
[[80,20],[50,40],[30,10]]

      [80,20]
[50,40]    [30,10]

1회전

dun = [80,20],[50,40],[30,10]
i = 0
count = 0
k = 80
d_value = [80, 20]
copy_dun = [50, 40] [30, 10]

-> in
dun = [50,40],[30,10]
i = 0
count = 1
k = 60
d_value = [50,40]
copy_dun = [30, 10]

->-> inin
dun = [30,10]
i = 0
count = 2
k = 20
d_value = [30, 10]
if x

return 2

<- out
dun = [50,40],[30,10]
i = 0
count = 1
k = 60
d_value = [50,40]
copy_dun = [30, 10]
check = 2
answer = 2 

i = 1
count = 1
k = 60
d_value = [30, 10]
copy_dun = [50,40]

->->inin
dun = [50,40]
i = 0
count = 2
k = 50
d_value = [50,40]
copy_dun = []

->->-> ininin
dun = []
count = 3
return 3

'''


def solution(k, dungeons):
    global answer
    answer = -1

    def back_tracking(count, k, dun):
        global answer         
        
        for i, d_value in enumerate(dun):
            if d_value[0] <= k :
                copy_dun = dun.copy()
                copy_dun.pop(i)
                
                check = back_tracking(count+1, k-d_value[1], copy_dun)
                
                print(check)
                
                if answer < check:
                    answer = check
    
        return count
    
    count = 0
    back_tracking(count, k, dungeons)
    
    return answer
