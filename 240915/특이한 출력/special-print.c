#include <stdio.h>

int main() {
    int i,j,n;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("(%d, %d) ", i,j,j*i);
            if((i+j)%4==0){
                printf("\n");
            }
        }
    }
    return 0;
}