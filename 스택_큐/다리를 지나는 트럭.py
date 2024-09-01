'''
트럭 여러 대 다리를 건넘
모든 트럭 다리를 건너는 데 몇 초 걸리는지 리턴
완전히 올라가지 않은 트럭 무게는 무시


bridge_length = 다리에 올라갈 수 있는 트럭 최대 수, 차량이 건너는 다리 길이 수 (1초에 1칸, 2면 2초 걸림)
weight = 다리가 견디는 트럭 무게
truck_weights = 트럭 별 무게 배열

'''

def solution(bridge_length, weight, truck_weights):
    answer = 0  # 경과 시간
    bridge = [0] * bridge_length  # 다리 위에 있는 트럭을 관리할 리스트
    total_weight_on_bridge = 0  # 현재 다리 위에 있는 트럭의 총 무게
    
    while bridge:  # 다리에 트럭이 남아있는 동안 반복
        answer += 1  # 시간 경과
        total_weight_on_bridge -= bridge.pop(0)  # 다리에서 트럭이 한 칸씩 이동 (가장 앞의 트럭이 나감)
        
        if truck_weights:  # 대기 중인 트럭이 남아있다면
            if total_weight_on_bridge + truck_weights[0] <= weight:  # 다리 무게 제한 내에서 추가 가능
                truck = truck_weights.pop(0)  # 대기 중인 첫 번째 트럭을 올림
                bridge.append(truck)  # 트럭이 다리에 올라감
                total_weight_on_bridge += truck  # 다리 위 트럭 무게 갱신
            else:
                bridge.append(0)  # 트럭을 올릴 수 없으면 빈 공간 유지

    return answer
