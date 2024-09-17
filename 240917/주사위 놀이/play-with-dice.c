#include <stdio.h>

int main() {
    int n,i,c_arr[7]={0,},arr[10];
    for(i=0;i<10;i++){
        scanf("%d", &arr[i]);
        c_arr[arr[i]]++;
    }
    for(i=1;i<7;i++){
        printf("%d - %d\n",i, c_arr[i]);
    }
    return 0;
}