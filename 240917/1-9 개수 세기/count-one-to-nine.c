#include <stdio.h>

int main() {
    int n,i,c_arr[10]={0,};
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
        c_arr[arr[i]]++;
    }
    for(i=1;i<10;i++){
        printf("%d\n", c_arr[i]);
    }
    return 0;
}