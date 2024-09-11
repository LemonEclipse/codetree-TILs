#include <stdio.h>
#include <stdbool.h>
int main() {
    int a,b,c,i;
    bool k = true;
    scanf("%d %d %d" ,&a,&b,&c);
    for(i=a;i<=b;i++){
        if(c%i!=0){
            k=false;
        }
    }
    if(k==false){
        printf("YES");
    }
    else{
        printf("NO");
    }
    return 0;
}