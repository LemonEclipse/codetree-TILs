#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);
    for(i=1;i<=n*2;i++){
        if(i%2==0){
            for(j=1;j<= 1 + (i / 2);j++){
                printf("* ");
            }
            printf("\n");
        }
        else{
            for(j=1;j<=  n - (i - 1) / 2;j++){
                printf("* ");
            }
            printf("\n");
        }
    }
    return 0;
}