#include <stdio.h>

int main() {
	// 변수 선언 및 입력
	int n;
	scanf("%d", &n);
	int cnt = 0;
	
    while(1) {
		// n이 1이 될 때까지 홀수일 때는 n = 3n+1을, 짝수일 때는 n = n/2를 반복합니다.
		if(n == 1)
			break;
		
		if(n % 2 == 1)
			n = 3 * n + 1;
		else
			n = n / 2;
		
		cnt++;
    }
	
	printf("%d", cnt);
	
    return 0;
}