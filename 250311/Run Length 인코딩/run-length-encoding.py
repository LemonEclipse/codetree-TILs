def run_length_encoding(s):
    if not s:
        return ""

    result = ""  # 최종 압축 결과 저장
    char_count = {}  # 현재 문자와 개수를 저장하는 딕셔너리
    prev_char = s[0]  # 첫 번째 문자 초기화
    char_count[prev_char] = 1  # 첫 문자는 1부터 시작

    for i in range(1, len(s)):
        if s[i] == prev_char:
            char_count[prev_char] += 1  # 같은 문자가 나오면 개수 증가
        else:
            # 이전 문자와 개수 저장 후, 새로운 문자로 변경
            result += f"{prev_char}{char_count[prev_char]}"
            prev_char = s[i]  # 새로운 문자 설정
            char_count = {prev_char: 1}  # 새로운 문자 카운트 시작

    # 마지막 문자 처리
    result += f"{prev_char}{char_count[prev_char]}"

    return result

# 입력 받기
A = input().strip()
print(run_length_encoding(A))
