#include <stdio.h>

int main() {
    int i,j,n,cnt=65;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=0;j<i-1;j++){
            printf("  ");
        }
        for(j=n-i+1;j>=1;j--){
            printf("%c ", cnt);
            cnt+=1;
            if(cnt>=91){
                cnt=65;
            }
            
        }
        
        printf("\n");
    }
    return 0;
}