#include <stdio.h>

int main() {
    int a, b, cnt = 0, c_arr[11] = {0}, sum = 0;
    scanf("%d %d", &a, &b);

    int temp_a = a;  // a 값을 유지하기 위해 복사본 사용

    // 몫이 0이 될 때까지 나누기
    while (temp_a > 0) {
        temp_a /= b;
        cnt++;
    }

    int arr[cnt];  // cnt 크기의 배열 선언

    // 나머지를 구하는 과정
    for (int i = 0; i < cnt; i++) {
        int k = a % b;
        arr[i] = k;
        a /= b;  // a를 갱신
    }

    // 나머지를 카운팅하는 배열 생성
    for (int i = 0; i < cnt; i++) {
        c_arr[arr[i]]++;
    }

    // c_arr 배열에서 제곱합 계산
    for (int i = 0; i < 10; i++) {
        sum += c_arr[i] * c_arr[i];  // 누적 합계 계산
    }

    // 결과 출력
    printf("%d", sum);

    return 0;
}