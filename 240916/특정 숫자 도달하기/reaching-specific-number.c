#include <stdio.h>

int main() {

	int arr[10];
	int val, sum_val;
	sum_val = 0;
	for (int i = 0; i < 10; i++) {
		scanf("%d", &arr[i]);
		sum_val += arr[i];
	}
	printf("%d %.1lf", sum_val,sum_val/10);

	return 0;

}