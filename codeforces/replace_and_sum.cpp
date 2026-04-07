#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// build prefix sum by greedy taking this choice to make the final array and use the poitners to get the maximum sum
int solve(vector<int> a, vector<int> b, int l, int r){
    int n = a.size();
    vector<long long> best(n);
    vector <long long> optimal(n);

    for (int i = 0; i < n; i++) {
        best[i] = max({a[i], b[i]});
    }

    // build optimal array
    optimal[n - 1] = best[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        optimal[i] = max(best[i], optimal[i + 1]);

    }
     vector<long long> prefix(n + 1, 0);                 
    for (int i = 0; i < n; i++) {                                                                                                                 
      prefix[i + 1] = prefix[i] + optimal[i]; }

    //get prefix ums from optimal array and return ans
    return (prefix[r] - prefix[l - 1]);
}

int main() {
    vector<int> a = {3, 1, 2};
    vector<int> b = {1, 2, 3};
    cout << solve(a, b, 1, 3) << endl;
    return 0;
}