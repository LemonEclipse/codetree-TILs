#include <stdio.h>

int main() {
    int n,i,j,cnt=0;
    int arr[4];
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        int sum_val=0;
        for(j=1;j<=4;j++){
            scanf(" %d", &arr[j]);
            sum_val+=arr[j];
        }
        double avg = sum_val/4;
        if(avg>=60){
            printf("pass\n");
            cnt+=1;
        }
        else{
            printf("fail\n");
        }
    }
    printf("%d", cnt);
    return 0;
}