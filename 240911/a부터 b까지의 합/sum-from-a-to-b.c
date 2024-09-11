#include <stdio.h>

int main() {
    int a,b,sum=0,i;
    scanf("%d %d",&a,&b);
    for(i=0;i<=b-a;i++){
        sum+=i;
    }
    printf("%d", sum);
    return 0;
}