#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("%d * %d = %d", i,j,i*j);
            if(j<n){
                printf(", ");    
            }
        }
        printf("\n");
    }
    return 0;
}