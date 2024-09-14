#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ", 11+j*2+i*2);
        }
        printf("\n");
    }
    return 0;
}