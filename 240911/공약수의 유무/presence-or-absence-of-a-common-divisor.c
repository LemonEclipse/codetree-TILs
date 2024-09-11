#include <stdio.h>
#include <stdbool.h>
int main() {
    int a,b,i;
    bool k=false;
    scanf("%d %d",&a,&b);
    for(i=a;i<=b;i++){
        if(1920%i==0 && 2880%i==0){
            k=true;
        }
    }
    if(k==true){
        printf("1");
    }
    else{
        printf("0");
    }
    return 0;
}