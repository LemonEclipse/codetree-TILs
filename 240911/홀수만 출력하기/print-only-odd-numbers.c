#include <stdio.h>

int main() {
    int N,b=0;
    scanf("%d", &N);
    while(1){
        int a;
        b+=1;
        if(b>N){
            break;
        }
        int K= scanf("%d",&a);
        if (a%2==1 && a%3==0){
            printf("%d\n", a);
        }

    }
    return 0;
}