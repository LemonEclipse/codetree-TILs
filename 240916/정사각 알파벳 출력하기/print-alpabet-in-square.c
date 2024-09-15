#include <stdio.h>

int main() {
    int i,j,n;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=65;j<=n+64;j++){
            printf("%c", i+j-1);
        }
        printf("\n")
    }
    return 0;
}