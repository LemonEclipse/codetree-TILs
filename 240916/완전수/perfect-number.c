#include <stdio.h>

int main() {
    int start,end,i,sum=0,cnt=0,j;
    scanf("%d %d", &start,&end);

    for(i=start;i<=end;i++){
        for(j=1;j<=i;j++){
            if(i%j==0 &&i!=j){
                sum+=j;
            }
        }
        if(i==sum){
            cnt+=1;
        }
    }
    printf("%d", cnt);
    return 0;
}