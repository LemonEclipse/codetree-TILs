#include <stdio.h>

int main() {
    int a=0,b=0,i=1;
    for(i;i<=10;i++){
        int n;
        scanf("%d", &n);
        if(n%3==0){
            a++;
        }
        if(n%5==0){
            b++;
        }
    }
    printf("%d %d", a,b);
    return 0;
}