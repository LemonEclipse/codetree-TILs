#include <stdio.h>

int main() {

	int cnt = 1;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 4; j++) {
			printf("%d ", cnt);
			cnt++;
		}
		printf("\n");
	}

	return 0;

}