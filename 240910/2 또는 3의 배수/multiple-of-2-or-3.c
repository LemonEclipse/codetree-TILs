#include <stdio.h>

int main() {
    int i=1,n;
    scanf("%d", &n);
    for(i;i<=n;i++){
        if (i%2==0 || i%3==0){
            printf("1 ");
        }
        else{
            printf("0 ");
        }
    }
    return 0;
}