#include <iostream>
using namespace std;

int main() {
    int n,i,j;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=(2*n)-(i*2);j>=1;j--){
            printf(" ");
        }
        for(j=1;j<=2*i-1;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}