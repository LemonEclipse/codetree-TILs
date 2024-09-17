#include <stdio.h>

int main() {
    int i,arr[100],n;
    scanf("%d", &n);
    arr[1]= n;
    arr[0] = 1;
    printf("%d %d ", arr[0],arr[1]);
    for(i=2;i<100;i++){
        arr[i]=arr[i-1]+arr[i-2];
        printf("%d ", arr[i]);
        
        if(arr[i]>100){
            break;
        }
    }
    return 0;
}