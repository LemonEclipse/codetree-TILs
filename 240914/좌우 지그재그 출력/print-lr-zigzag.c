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
            int k=cnt+n-1;
            for(j=k;j>=cnt;j--){
                printf("%d ", j);
                
            }
            cnt=k+1;
        }
		printf("\n");
	}

	return 0;

}