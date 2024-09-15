#include <stdio.h>

int main() {
    int n,cnt=0,i;

    scanf("%d", &n);

    for(i=1;i<=n;i++){
        int a;
        scanf("%d", &a);
        while (n != 1) {
            if (n % 2 == 0) {  
                n /= 2;
            } else {           
                n = n * 3 + 1;
            }
            cnt++;
        }
        printf("%d\n", cnt);
    }    

    
    return 0;
}