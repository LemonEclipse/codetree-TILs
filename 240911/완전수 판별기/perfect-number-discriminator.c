#include <stdio.h>

int main() {
    int n,i=1,sum=0;
    scanf("%d", &n);
    for(i;i<n;i++){
        if(n%i==0){
            sum+=i;
        }
    }
    if(n==sum){
        printf("P");
    }
    else{
        printf("N");
    }
    return 0;
}