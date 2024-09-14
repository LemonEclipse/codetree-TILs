#include <stdio.h>

int main() {
    int n,i,j;
    int cnt=1;
    scanf("%d", &n);

	for (i = 1; i <=n; i++) {
		if(i%2!=0){
            for(j=1;j<=n;j++){
                printf("%d ",cnt);
                cnt++;
            }
        }
        else{
            for(j=1;j<=n;j++){
                printf("%d ", cnt+1);
                cnt+=2;
            }
          
        }
		printf("\n");
	}

	return 0;

}