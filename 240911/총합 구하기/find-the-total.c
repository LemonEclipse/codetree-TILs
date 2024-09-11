#include <stdio.h>

int main() {
    int a,b,i=0,sum=0;
    scanf("%d %d", &a,&b);
    int k=a;
    for(i;i<=b-a;i++){
        if(k%6==0 && k%8!=0){
            sum+=k;
            
        }
        k++;
    }
    printf("%d", sum);
    return 0;
}