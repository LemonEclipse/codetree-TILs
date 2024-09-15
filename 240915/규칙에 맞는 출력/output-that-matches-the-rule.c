#include <stdio.h>

int main() {
    int n,i,j;
    
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        
        for(j=1;j<=i;j++){
            int k=i-j;
            printf("%d ", n-k);
            k++;
        }
        
        printf("\n");
    }
    return 0;
}