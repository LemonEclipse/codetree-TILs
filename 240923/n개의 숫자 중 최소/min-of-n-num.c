#include <stdio.h>

int main() {
    int n,icnt=0;
    scanf("%d", &n);
    int arr[n];
    for(int k=1;k<=n;k++){
        scanf("%d", &arr[k]);
    }
    int min=arr[0];
    for(i=1;i<=n;i++){
        if(arr[i]<min){
            min=arr[i];
        }
    }
    for(i=1;i<=n;i++){
        if(arr[i]==min){
            cnt++;
        }
    }
    printf("%d %d", min, cnt);
    return 0;
}