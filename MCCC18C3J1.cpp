#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    int sum = 0;
    for (int i=0; i<n; i++) {
        int a;
        cin >> a;
        sum += a;
    }
    cout << sum << "\n";
}

int main() {
    solve();
    return 0;
}
