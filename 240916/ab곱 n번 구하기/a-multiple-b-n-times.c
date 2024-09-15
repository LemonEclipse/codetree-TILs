#include <stdio.h>

int main() {

	int n;
    scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int a, b,k=1;
		scanf("%d %d", &a, &b);

		for (int j = a; j <= b; j++) {
			k *= j;
		}
		printf("%d\n", k);
        
	}

	return 0;

}