#include <stdio.h>

int main() {
    int n,i,sum_val=0;
    
    int arr[10];
    for(i=0;i<10;i++){
        scanf(" %d", &arr[i]);
        if(i==2||i==4||i==9){
            sum_val+=arr[i];
        }
    }
    printf("%d", sum_val);

    return 0;
}