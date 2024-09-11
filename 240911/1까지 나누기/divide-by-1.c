#include <stdio.h>

int main() {
    int n,i=01;
    scanf("%d", &n);
    while(1){
        n/=i;
        
        
        if(n<=1){
            break;
        }
        i++;
    }
    printf("%d", i);
    return 0;
}