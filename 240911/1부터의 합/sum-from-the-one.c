#include <stdio.h>

int main() {
    int a,i=1,sum=0,cnt=0;
    scanf("%d", &a);
    for(i;i<=a;i++){
        sum+=i;
        cnt+=1;
        if(sum>=a){
            break;
        }
    }
    printf("%d", cnt);
    return 0;
}