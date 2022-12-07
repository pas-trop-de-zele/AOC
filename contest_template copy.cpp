#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define vd vector<double>
#define vvd vector<vd>
#define vll vector<ll>
#define vvll vector<vll>
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pi pair<int, int>
#define vpi vector<pi>
#define vvpi vector<vpi>

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

double euclid_dist(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void solve() {
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}