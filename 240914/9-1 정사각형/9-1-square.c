#include <stdio.h>

int main() {

	int cnt = 9;
    int n,i,j;
    scanf("%d", &n);
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%d", cnt);
            if(cnt==1){
                cnt=10;
            }
			cnt--;
		}
		printf("\n");
	}

	return 0;

}