from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request) :
    import math           # math 모듈 불러 오기

    old_pi = 3.14163      # 아르키메데스가 96각형을 사용(n = 96)하여 계산한 원주율값
    n = 5                 # 5각형부터 시작
    err = 0.000000001          # 허용오차 십억분의 일

    while True:
        degree = 360 / n      # n각형의 내각
        theta = degree / 2    # 내각의 절반이 삼각함수의 기준 각도(A)
        inner_length = math.sin(math.radians(theta)) * 2      # 내접하는 변의 길이 sin A * 2
        outer_length = math.tan(math.radians(theta)) * 2      # 외접하는 변의 길이 tan A * 2
        difference = outer_length - inner_length              # 내접하는 변과 외접하는 변의 길이 차이
        new_pi = n * ((outer_length + inner_length) / 2) /2   # 중간값으로 원주율 계산

        # n값 증가에 따른 원주율 값, 오차 변화
        # print("n: ", n, "new_pi: ", new_pi)
        if (difference < err): 
            break                # 반복문 탈출
        else:
            n = n + 1            # 다각형의 변의 개수를 늘리기
            
    # 아르키메데스의 원주율과 계산값 차이 비교
    # print("old_pi: ", old_pi, "new_pi: ", new_pi, "error: ", new_pi - old_pi)

    # 파이썬 내장 원주율값(math.pi)와 비교
    # print("내장 원주율: ", math.pi, "차이: ", math.pi - new_pi)

    httptext = f"""내장원주율 {math.pi}, 차이 {math.pi - new_pi}"""
    return HttpResponse(httptext)