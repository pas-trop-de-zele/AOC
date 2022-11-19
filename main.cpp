#include <bits/stdc++.h>
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

void deb(const vi &v) {
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

template <typename T>
void deb(T a) {
    cout << a << endl;
}

void solve() {
    int n;
    cin >> n;
    vll sides;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        sides.push_back(a);
    }
    sort(sides.begin(), sides.end());
    for (int i = 0; i < sides.size() - 2; ++i) {
        if (i > 0 && sides[i] == sides[i - 1]) {
            continue;
        }
        int l = i + 1, r = sides.size() - 1;
        while (l < r) {
            if (sides[l] + sides[r] > sides[i] && sides[i] + sides[r] > sides[l] && sides[i] + sides[l] > sides[r]) {
                cout << "YES" << endl;
                return;
            } else {
                ++l;
                while (l + 1 < r && sides[l] == sides[l - 1]) {
                    ++l;
                }
            }
        }
    }
    for (int i = 0; i < sides.size() - 2; ++i) {
        if (i > 0 && sides[i] == sides[i - 1]) {
            continue;
        }
        int l = i + 1, r = sides.size() - 1;
        while (l < r) {
            if (sides[l] + sides[r] > sides[i] && sides[i] + sides[r] > sides[l] && sides[i] + sides[l] > sides[r]) {
                cout << "YES" << endl;
                return;
            } else {
                --r;
                while (l < r - 1 && sides[r] == sides[r + 1]) {
                    --r;
                }
            }
        }
    }

    cout << "NO" << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}