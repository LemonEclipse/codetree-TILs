#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);
    for(i=1;i<=n*2;i++){
        if(i%2!=0){
            for(j=n;j>i-(i/2)-1;j--){
                printf("* ");
            }
            printf("\n");
        }
        else{
            for(j=1;j<=(i/2);j++){
                printf("* ");
            }
            printf("\n");
        }
    }
    return 0;
}