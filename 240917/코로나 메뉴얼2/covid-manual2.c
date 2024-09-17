#include <stdio.h>

int main() {
    int arr[3],arr2[4],i;
    char arr_c[3];
    for(i=0;i<3;i++){
        scanf("%c %d", &arr_c[i],&arr[i]);
        if(arr_c[i]=='Y'){
                if(arr[i]>=37){
                    arr2[0]++;
                }
                else{
                    arr2[2]++;
                }
        }
        else{
            if(arr[i]>=37){
                arr2[1]++;
            }
            else{
                arr2[3]++;
            }
        }
    }
    for(i=0;i<4;i++){
            printf("%d ", arr2[i]);
        }
    if(arr2[0]>=2){
        printf("E");
    }
    return 0;
}