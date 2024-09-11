#include <stdio.h>

int main() {
    int n,i=1,cnt=0;
    scanf("%d", &n);
    for(i;i<=n;i++){
        if(i%2==0 || i%3==0 || i%5==0){
            continue;
        }
        else{
            cnt+=1;
        }
    }
    printf("%d", cnt);
    return 0;
}