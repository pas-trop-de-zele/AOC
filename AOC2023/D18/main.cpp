#include <assert.h>
#include <limits.h>
#include <math.h>

#include <algorithm>
#include <bit>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
#define ll long long
#define ld long double
#define vll vector<ll>
#define vvll vector<vll>
#define vi vector<int>
#define vvi vector<vi>
#define vvvi vector<vvi>
#define vs vector<string>
#define pi pair<int, int>
#define vpi vector<pi>
#define vvpi vector<vpi>
#define pll pair<ll, ll>
#define ppll pair<pll, pll>
#define vpll vector<pll>
#define vvpll vector<vpll>
#define PB push_back
#define all(x) x.begin(), x.end()
#define ff first
#define ss second
double EPS = 1e-18;
// const vpi MOVES_ADJACENT{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
// const vpi MOVES_ALL{{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0,
// -1}, {1, -1}};

template <typename T>
void db(T const& coll) {
    typename T::const_iterator pos;
    typename T::const_iterator end(coll.end());

    for (pos = coll.begin(); pos != end; ++pos) {
        cout << *pos << ' ';
    }
    cout << "\n";
}

void ans(ll x) { cout << (x == 0 ? "YES" : "NO") << "\n"; }

double polygonArea(double X[], double Y[], int n)
{
    // Initialize area
    double area = 0.0;
 
    // Calculate value of shoelace formula
    int j = n - 1;
    for (int i = 0; i < n; i++)
    {
        area += (X[j] + X[i]) * (Y[j] - Y[i]);
        j = i;  // j is previous vertex to i
    }
 
    // Return absolute value
    return abs(area / 2.0);
}

void solve() {
    ll n;
    cin >> n;
    ll y = 0, x = 0;
    vll X{0};
    vll Y{0};
    set<pll> seen;
    seen.insert({y,x});
    for (ll i = 0; i < n; ++i) {
        ll dy,dx,val;
        cin >> dy >> dx >> val;
        for (ll j = 0; j < val; ++j) {
            y += dy;
            x += dx;
            X.PB(y);
            Y.PB(x);
            seen.insert({y,x});
        }
    }
    X.PB(0); Y.PB(0); // complete loop
    double area = 0.0;

    ll LOOPN = X.size();
    int j =  - 1;
    for (int i = 0; i < LOOPN; i++)
    {
        cout << LOOPN - i << "\n";
        area += (X[j] + X[i]) * (Y[j] - Y[i]);
        j = i;  // j is previous vertex to i
    }
    double A = abs(area / 2.0);

    cout << fixed << setprecision(2) << (A + 1 + ((double)seen.size() / 2.0)) << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // init();
    // ll t;
    // cin >> t;
    // while (t--) {
    //     solve();
    // }

    solve();
}