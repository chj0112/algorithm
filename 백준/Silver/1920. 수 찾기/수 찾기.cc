#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, m, num;
	int a[100001];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		a[i] = num;
	}
	sort(a, a + n);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> num;
		cout << int(binary_search(a, a + n, num)) << '\n';
	}
	return 0;
}