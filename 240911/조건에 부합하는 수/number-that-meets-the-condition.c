#include <stdio.h>

int main() {
    int a,i=1;
    scanf("%d", &a);
    for(i;i<=a;i++){
        if(i%2==0 && i%4!=0){
            continue;
        }
        if((i/8)%2==0){
            continue;
        }
        if((i%7)<4){
            continue;
        }
        printf("%d ", i);
    }
    return 0;
}