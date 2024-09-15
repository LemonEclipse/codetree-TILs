#include <stdio.h>

int main() {
    int n,m,cnt=0,i;

    scanf("%d", &n);

    for(i=1;i<=n;i++){
        
        scanf("%d", &m);
        while (m != 1) {
            if (m % 2 == 0) {  
                m /= 2;
            } else {           
                m = m * 3 + 1;
            }
            cnt++;
        }
        printf("%d\n", cnt);
        cnt=1;
    }    

    
    return 0;
}