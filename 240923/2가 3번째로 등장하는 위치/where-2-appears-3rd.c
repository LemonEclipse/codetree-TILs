#include <stdio.h>

int main() {
    int n,i,cnt=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
        if(arr[i]==2){
            cnt++;
        }
        if(cnt==3){
            printf("%d", i+1);
            break;
        }
    }
    return 0;
}