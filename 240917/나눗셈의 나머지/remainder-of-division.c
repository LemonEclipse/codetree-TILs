#include <stdio.h>
#include <stdio.h>

int main() {
    int a, b;
    int remainder_count[10] = {0};  // 나머지는 0부터 b-1까지 나올 수 있으므로 b는 10 이하이므로 최대 10칸 배열 선언
    int sum = 0;

    // a와 b 입력받기
    scanf("%d %d", &a, &b);

    // a가 1보다 클 때까지 반복
    while (a > 1) {
        int remainder = a % b;  // 나머지 계산
        remainder_count[remainder]++;  // 해당 나머지 등장 횟수 카운트
        a /= b;  // a를 b로 나눈 몫으로 갱신
    }

    // 등장 횟수의 제곱합 계산
    for (int i = 0; i < b; i++) {
        sum += remainder_count[i] * remainder_count[i];  // 제곱합 계산
    }

    // 결과 출력
    printf("%d\n", sum);

    return 0;
}