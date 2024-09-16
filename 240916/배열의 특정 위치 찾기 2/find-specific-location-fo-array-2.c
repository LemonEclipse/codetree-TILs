#include <stdio.h>

int main() {
    int n,i,sum_odd=0,sum_even=0;
    
    int arr[10];
    for(i=0;i<10;i++){
        scanf("%d", &arr[i]);
        if(i%2!=0){
            sum_odd+=arr[i];
        }
        else{
            sum_even+=arr[i];
        }
    }

    if(sum_even>=sum_odd){
        printf("%d", sum_even-sum_odd);
    }
    else{
        printf("%d", sum_odd-sum_even);
    }

    return 0;
}