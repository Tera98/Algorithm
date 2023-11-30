'''
12장 [파일과 예외처리] 과제 2번 Template

이 과제는 풀이 시 반드시 주석을 작성하세요.
'''


def calculate_revenue(file_path):

    total_sales = 0     # 정수들을 저장할 공간 생성

    try:
        file = open(file_path, 'r', encoding='UTF8')        # main 에서 받아온 경로를 이용해 파일 오픈
        for line in file:       # file 안 한 줄을 line 에 할당
            line = line.lstrip('1234567890일 매출액')       # 왼쪽 "()일 매출액" 을 제거 하는 부분
            total_sales += int(line.strip(':\n'))       # \n과 :를 제거 하는 strip 구문 후, 정수로 변환 하여 변수에 저장
        print(f"한달 총 매출: {total_sales}")            # 한달 총 매출 출력
        print(f"평균 일 매출: {total_sales // 31}")      # 12월 기준, 31을 나눠서 1일 평균 총 매출을 구함

    except Exception as e:      # 모든 Error 발생시 print 하는 구문 추가
        print(f"에러 발생: {e}")

    finally:        # 어떠한 경우에도 실행될 구문들
        print("실행 완료")
        print("-------------------\n학번 : 201701671\n이름 : 안원용")


if __name__ == '__main__':
    calculate_revenue("/Users/wonyong/Desktop/revenue.txt")     # 파일 경로
