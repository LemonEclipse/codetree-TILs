#include <stdio.h>
#include <stdbool.h>
int main() {
    int n,i=2;
    bool a=false;
    scanf("%d", &n);
    for(i;i<=n-1;i++){
        if(n%i==0){
            a=true;
        }
    }
    if(a==true){
        printf("C");
    }
    else{
        printf("N");
    }
    return 0;
}