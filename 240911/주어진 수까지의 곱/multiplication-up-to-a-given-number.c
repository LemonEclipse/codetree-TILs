#include <stdio.h>

int main() {
    int a,b,prod=1;
    scanf("%d %d", &a,&b);
    while(1){
        if(a>b){
            break;
        }
        prod*=a;
        a++;
    }
    printf("%d", prod);
    return 0;
}