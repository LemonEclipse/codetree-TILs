#include <stdio.h>

int main() {
    int n,i,sum_val=0,sum=0;
    
    int arr[10];
    for(i=0;i<10;i++){
        scanf("%d", &arr[i]);
        if(i%2!=0){
            sum_val+=arr[i];
        }
        if(i%3==2){
            sum+=arr[i];
        }
    }
    double avg = (double)sum/3;
    printf("%d %.1lf", sum_val, avg);

    return 0;
}