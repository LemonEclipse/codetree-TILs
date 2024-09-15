#include <stdio.h>

int main() {
    int a,b,i,j;
    scanf("%d %d", &a,&b);
    for(i=1;i<=9;i++){
       for(j=b;j>=a;j--){
        if(j%2==0){
            printf("%d * %d = %d",j,i,j*i);
            if(j>2){
                printf(" / ");
            }
        }
        
        }
        printf("\n");
    }
    return 0;
}