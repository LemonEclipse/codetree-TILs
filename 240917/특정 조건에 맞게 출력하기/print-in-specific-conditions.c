#include <stdio.h>

int main() {
    int i,arr[100];
    for(i=0;i<100;i++){
        scanf("%d", &arr[i]);
        if(arr[i]==0){
            break;
        }
        if(arr[i]%2!=0){
            arr[i]+=3;
            printf("%d ", arr[i]);
        }
        else{
            arr[i]=arr[i]/2;
            printf("%d ", arr[i]);
        }
    }
    return 0;
}