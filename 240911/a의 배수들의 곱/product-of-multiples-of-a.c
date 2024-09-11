#include <stdio.h>

int main() {
    int a,b,i=1,prod=1;
    scanf("%d %d", &a,&b);
    for(i;i<=b;i++){
        if(a%i==0){
            prod*=i
        }
    }
    printf("%d", prod);
    return 0;
}