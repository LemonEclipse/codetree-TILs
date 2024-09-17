#include <stdio.h>

int main() {

	char word[6] = { 'L', 'E', 'B', 'R', 'O' , 'S'},n;
    scanf("%c", &n);
    int cnt=0,a;

	for (int i = 0; i < 6; i++) {
		if (word[i] == n) {
			cnt+=1;
            a=i;
		}
	}
    if(cnt==1){
        printf("%d", a);
    }
    else{
        printf("None");
    }

	return 0;

}