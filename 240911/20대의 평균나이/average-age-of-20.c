#include <stdio.h>

int main() {
    int cnt=0,sum=0,n;
    while(1){
        scanf("%d", &n);
        if(30>n && n>10){
            sum+=n;
            cnt+=1;
        }
        else{
            break;
        }
    }
    printf("%.2lf",(double)sum/cnt);
    return 0;
}