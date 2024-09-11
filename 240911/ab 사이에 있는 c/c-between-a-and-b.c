#include <stdio.h>
#include<stdbool.h>
int main() {
    int a,b,c,i;
    bool k=false;
    scanf("%d %d %d", &a,&b,&c);
    for(i=a;i<=b;i++){
        if(i%c==0){
            k=true;
        }
        
    }
    if(k==true){
            printf("YES");
        }
    else{
            printf("NO");
        }
    return 0;
}