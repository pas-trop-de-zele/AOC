#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi>
#define vll vector<ll>
#define vvll vector<vl>
#define vs vector<string>
#define pi pair<int, int>
#define vpi vector<pi>

const vpi MOVES_ADJACENT{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
const vpi MOVES_ALL{{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};

template <typename T>
void deb(T a) {
    cout << a << endl;
}

template <typename T>
void deb(const vector<T> &v) {
    for (auto &c : v) {
        cout << c << " ";
    }
    cout << endl;
}

void deb(int *a, int n) {
    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;
}

template <typename T>
void deb(T *a, int n, int m) {
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            cout << a[r][c] << " ";
        }
        cout << endl;
    }
}

vll primeFac(ll n) {
    vll p;
    while (n % 2 == 0) {
        p.push_back(2);
        n /= 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        while(n % i == 0) {
            p.push_back(i);
            n /= i;
        }
        if (n == 1) {
            break;
        }
    }
    if (n > 1) {
        p.push_back(n);
    }
    return p;
}

template <typename T>
struct Counter {
    unordered_map<T, ll> counter;
    ll operator[](ll x) const {
        if (counter.find(x) == counter.end()) {
            counter[x] = 0;
        }
        return counter[x];
    }
    ll &operator[](ll x) {
        if (counter.find(x) == counter.end()) {
            counter[x] = 0;
        }
        return counter[x];
    }

    typename unordered_map<T, ll>::iterator begin() { return counter.begin(); }
    typename unordered_map<T, ll>::iterator end() { return counter.end(); }
};

void solve() {
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // int t;
    // cin >> t;
    // while (t--) {
    //     solve();
    // }
    solve();
}