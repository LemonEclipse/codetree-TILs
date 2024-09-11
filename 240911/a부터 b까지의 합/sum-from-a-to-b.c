#include <stdio.h>

int main() {
    int a,b,sum=0;
    scanf("%d %d", &a,&b);
    int k=a-1;
    for(int i=0;i<=b-a;i++){
        k++;
        sum+=k;
        
    }
    printf("%d", sum);
    return 0;
}