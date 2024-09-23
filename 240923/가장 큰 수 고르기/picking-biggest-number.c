#include <stdio.h>

int main() {
    int n,i,arr[10];
    for(int k=1;k<=10;k++){
        scanf("%d", &arr[k]);
    }
    int max=arr[0];
    for(i=1;i<=10;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    printf("%d", max);
    return 0;
}