

#include <unordered_map>

using std::unordered_map;


// Memoization
int memoization(int n, unordered_map<int, int> *cache) {
    if (n <= 1) {
        return n;
    }
    if (cache->count(n)) {
        return (*cache)[n];
    }
    (*cache)[n] = memoization(n - 1, cache) + memoization(n - 2, cache);
    return (*cache)[n];
}