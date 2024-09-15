#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);
    int cnt=1;
    for(i=1;i<=n;i++){
        
        for(j=1;j<=i;j++){
            
            printf("%d ", cnt);
            cnt++;
        }
        printf("\n");
       
    }
    return 0;
}