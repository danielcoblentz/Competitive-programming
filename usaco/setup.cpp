#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define all(x) (x).begin(), (x).end()
#define rep(i, a, b) for (int i = a; i < b; i++)

void fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

void solve() {
    int n;
    cin >> n;

    vi v(n);
    rep(i, 0, n) {
        cin >> v[i];
    }

    sort(all(v));

    for(int x : v) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    fast_io();

    int t = 1;
    while(t--) {
        solve();
    }

    return 0;
}
