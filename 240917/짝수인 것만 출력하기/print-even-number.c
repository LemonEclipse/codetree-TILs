#include <stdio.h>

int main() {
    int n,i;
    scanf("%d", &n);
    int arr[n];
    for(i=0;i<n;i++){
        int N_arr[i];
        scanf("%d", &arr[i]);
        if(arr[i]%2==0){
            N_arr[i]=arr[i];
            printf("%d ", N_arr[i]);
        }
    }
    
    return 0;
}