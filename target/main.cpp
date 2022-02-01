#include <stdio.h>

int main() {
	
	int n;
	scanf("%d", &n);

	int i;
	int res = 1;
	for (i = 2; i <= n; i++) {
		res *= i;
	}
	printf("%d", res);

	return 0;
}
