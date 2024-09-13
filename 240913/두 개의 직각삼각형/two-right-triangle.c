#include<stdio.h>

int main() {
    int n;
    scanf("%d", &n);  // 사용자로부터 정수 n 입력

    for(int i = 0; i < n; i++) {
        // 왼쪽 삼각형의 별 출력
        for(int j = 0; j < n - i; j++) {
            printf("*");
        }
        
        // 중간 공백 출력
        for(int j = 0; j < 2 * i; j++) {
            printf(" ");
        }
        
        // 오른쪽 삼각형의 별 출력
        for(int j = 0; j < n - i; j++) {
            printf("*");
        }
        
        // 줄바꿈
        printf("\n");
    }
    
    return 0;
}