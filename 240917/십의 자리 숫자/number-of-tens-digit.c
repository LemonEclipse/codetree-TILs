#include <stdio.h>

int main() {
    int i,arr[100],c_arr[10]={0,};
    for(i=0;i<100;i++){
        scanf("%d", &arr[i]);
        if(arr[i]==0){
            break;
        }
        else{
            if(arr[i]<10){
                continue;
            }
            else{
                c_arr[arr[i]/10]++;
            }
        }
    }
    for(i=1;i<=9;i++){
        printf("%d - %d\n", i, c_arr[i]);
    }
    return 0;
}