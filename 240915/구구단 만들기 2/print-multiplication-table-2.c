#include <stdio.h>

int main() {
    int a,b,i,j;
    scanf("%d %d", &a,&b);
    for(i=2;i<=8;i++){
        if(i%2==0){
            for(j=b;j>=a;j--){
                printf("%d * %d = %d", j,i,j*i); 
                if(j>a){
                printf(" / ");
            }
            }
           printf("\n");
        }
        
    }
    return 0;
}