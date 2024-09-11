#include <stdio.h>
#include <stdbool.h>
int main() {
    int a,i;
    bool k=true;
    for(i=1;i<=5;i++){
        scanf("%d", &a);
        if(a%3!=0){
            k=false;
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