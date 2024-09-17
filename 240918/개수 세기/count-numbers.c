#include <stdio.h>

int main() {
    int n,m,i,k,cnt=0;

    scanf("%d %d", &n,&m);
    int arr[n];
    for(i=0;i<n;i++){
        scanf("%d ", &arr[i]);
        if(arr[i]==m){
            cnt+=1;
        }
    }
    printf("%d", cnt);
    return 0;
}