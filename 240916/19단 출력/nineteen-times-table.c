#include <stdio.h>

int main() {
    int i,j;
    
    for(i=1;i<=19;i++){
        for(j=1;j<=19;j++){
            printf("%d * %d = %d", i,j,j*i);
            if(j%2==0 || j==19){
                printf("\n");
            }
            else{
                printf(" / ");
            }
        }
    }
    return 0;
}