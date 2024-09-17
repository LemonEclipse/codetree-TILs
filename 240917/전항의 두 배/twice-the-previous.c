#include <stdio.h>

int main() {
    int i,arr[10];
    scanf("%d %d", &arr[0], &arr[1]);
    printf("%d %d ", arr[0],arr[1]);
    for(i=2;i<10;i++){
        arr[i]=arr[i-1]+arr[i-2]*2;
        printf("%d ", arr[i]);

    }
    return 0;
}