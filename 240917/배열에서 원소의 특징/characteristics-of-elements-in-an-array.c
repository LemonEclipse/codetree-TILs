#include <stdio.h>

int main() {
    int i,n;
    int arr[10];
    for(i=0;i<10;i++){
        scanf("%d", &arr[i]);
        if(arr[i]%3==0){
            printf("%d", arr[i-1]);
            break;
        }
        
    }
    return 0;
}