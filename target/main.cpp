#include <bits/stdc++.h>

using namespace std;


int main() {
	
	int n;
	cin >> n;

	char a[n], b[n];
	int counter = 0;
	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < n; i++) {
		cin >> b[i];
		if (a[i] != b[i]) counter++;
	}
	cout << counter;
	
	return 0;
}
