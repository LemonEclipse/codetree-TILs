#include <stdio.h>

int main() {
    int n,i,j,k;
    scanf("%d", &n);
    for(k=1;k<=2;k++){
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                printf("*");
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}