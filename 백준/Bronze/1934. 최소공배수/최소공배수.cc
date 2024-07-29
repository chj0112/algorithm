#include <iostream>

using namespace std;

int main() {
    int t, a, b;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        int min, max;
        if (a < b) {
            min = a;
            max = b;
        } else {
            min = b;
            max = a;
        }
        int plus = max;
        for (int j = 0; j < min; j++) {
            if (max % min == 0) {
                cout << max << '\n';
                break;
            } else {
                max += plus;
            }
        }
    }
}