#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d", &n);

	for (i = 0; i < n; i++) {
		if (i % 2 == 0) {
			for (j = 0; j < n; j++) {
				printf("%d", j + 1);
			}
		}
		else {
			for (j = 0; j < n; j++) {
				printf("%d", n - j);
			}
		}
		printf("\n");
	}

	return 0;

}