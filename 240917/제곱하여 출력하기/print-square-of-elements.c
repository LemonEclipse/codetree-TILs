#include <stdio.h>

int main() {
    int n,i;
    scanf("%d", &n);
    int arr[100],arr_2[100];
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        arr[i]=arr[i]*arr[i];
        printf("%d ",arr[i]);
    }
    return 0;
}