from django.shortcuts import render, HttpResponse
import math

# Create your views here.
def main_page(request) :

    html_tag = """
    <center><a type="button" href="pi">pi</a></center>
    """
    return HttpResponse(html_tag)


def answer_pi(request) :

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
            

    
    html_tag = f"""
    {math.pi}
    <center><button type="button" style="width:150px;height:80px;" class="btn btn-outline-success" onclick="history.back()">이전으로</button></center>
    """

    return HttpResponse(html_tag)