#include <stdio.h>

int main() {
    int n,i,j,cnt=1;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=0;j<i-1;j++){
            printf("  ");
        }
        for(j=n-i+1;j>=1;j--){
            printf("%d ", cnt);
            cnt++;
        }
        if(cnt>9){
            cnt=1;
        }
        printf("\n");
        
    }
    return 0;
}