#include <stdio.h>

int main() {
    int n,i,cnt=0;
    scanf("%d", &n);
    int arr[n];
    for(int k=0;k<n;k++){
        scanf("%d", &arr[k]);
    }
    int min=arr[0];
    for(i=0;i<n;i++){
        if(arr[i]<min){
            min=arr[i];
        }
    }
    for(i=0;i<n;i++){
        if(arr[i]==min){
            cnt++;
        }
    }
    printf("%d %d", min, cnt);
    return 0;
}