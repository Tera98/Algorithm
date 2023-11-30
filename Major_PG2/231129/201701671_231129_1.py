'''
12장 [파일과 예외처리] 과제 1번 Template
'''

try:
    with open("/Users/wonyong/Desktop/prelude.txt", 'r', encoding='UTF8') as file:
        # 텍스트 파일 읽기
        space_count, total_char_count, word_count = 0, 0, 0     # 변수 생성

        for line in file:       # file 한 줄을 line 에 저장
            space_count += line.count(" ")      # 공백 수를 저장
            word_count += line.count(" ") + 1       # 단어 수 = 공백 수 + 1 (한 줄 기준)
            total_char_count += len(line)       # 총 글자수 저장
        non_space_char_count = total_char_count - word_count + 1
        # 총 글자 수에서 줄바꿈 문자(\n)을 포함한 공백을 지우기 위해 총 단어 수를 이용 하였다.

        # 공백 수 출력
        print(f"공백 수: {space_count}")
        # 공백을 제외한 문자 수 출력
        print(f"공백을 제외한 문자 수: {non_space_char_count}")
        # 공백을 포함한 문자 수 출력
        print(f"공백을 포함한 문자 수: {total_char_count}")
        # 단어 수 출력
        print(f"단어 수: {word_count}")
        print("-------------------\n학번 : 201701671\n이름 : 안원용")

except Exception as e:      # 모든 Error 발생시 print 하는 구문 추가
    print(f"에러 발생: {e}")
