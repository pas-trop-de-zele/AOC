#include <algorithm>
#include <assert.h>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits.h>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <bit>
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
#define vpll vector<pll>
#define pb push_back
#define all(x) x.begin(), x.end()
#define inf LLONG_MAX
#define neginf LLONG_MIN
const vpi MOVES_ADJACENT{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
// const vpi MOVES_ALL{{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};
template <typename T>
void deb(T a)
{
    cout << a << endl;
}

template <typename T>
void deb(const vector<T> &v)
{
    for (int i = 0; i < v.size(); ++i)
    {
        cout << v[i] << (i < v.size() - 1 ? " " : "");
    }
    cout << endl;
}

void deb(int *a, int n)
{
    for (int i = 0; i < n; ++i)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

template <typename T>
void deb(T *a, int n, int m)
{
    for (int r = 0; r < n; ++r)
    {
        for (int c = 0; c < m; ++c)
        {
            cout << a[r][c] << " ";
        }
        cout << endl;
    }
}

vll getPrimeFacs(ll n)
{
    vll p;
    while (n % 2 == 0)
    {
        p.push_back(2);
        n /= 2;
    }
    for (int i = 3; i * i <= n; i += 2)
    {
        while (n % i == 0)
        {
            p.push_back(i);
            n /= i;
        }
        if (n == 1)
        {
            break;
        }
    }
    if (n > 1)
    {
        p.push_back(n);
    }
    return p;
}

ll fast_pow(ll a, ll b, ll m)
{
    ll ret = 1;
    while (b)
    {
        if (b & 1)
        {
            ret *= a;
            ret %= m;
        }
        a *= a;
        a %= m;
        b >>= 1;
    }
    return ret;
}

ll gcd(ll a, ll b)
{
    return a ? gcd(b % a, a) : b;
}

ll lcm(ll a, ll b)
{
    return (a * b) / gcd(a, b);
}

void solve()
{
}

int main()
{
    ios::sync_with_stdio(0);
    // cin.tie(0);
    // ll t;
    // cin >> t;
    // while (t--)
    // {
    //     solve();
    // }
    solve();
}
