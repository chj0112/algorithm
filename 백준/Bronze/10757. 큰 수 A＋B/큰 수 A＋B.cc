#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a, b;
    string result = "";
    int carry = 0;
    cin >> a >> b;
    if (a.length() > b.length()) {
        int k = a.length() - b.length();
        for (int i = 0; i < k; i++) {
            b = '0' + b;
        }
    } else if (a.length() < b.length()) {
        int k = b.length() - a.length();
        for (int i = 0; i < k; i++) {
            a = '0' + a;
        }
    }
    int length = a.length();
    for (int i = 1; i < length + 1; i++) {
        int temp = a[length - i] + b[length - i] + carry - '0' - '0';
        result = to_string(temp % 10) + result;
        carry = temp / 10;
    }
    if (carry != 0) result = to_string(carry) + result;
    cout << result;

    return 0;
}