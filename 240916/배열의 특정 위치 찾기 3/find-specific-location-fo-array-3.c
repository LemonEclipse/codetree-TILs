#include <stdio.h>

int main() {
    int arr[100];
    int k;

	for(int i = 0; i < 100; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] == 0){
			k = i;
			break;
		}
	}

    printf("%d", arr[k - 3] + arr[k - 2] + arr[k - 1]);

    return 0;
}