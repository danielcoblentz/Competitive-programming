// Dynamic Programming
int fib(int n) {
    if (n < 2) {
        return n;
    }

    int dp[] = {0, 1};
    int i = 2;
    while (i <= n) {
        int tmp = dp[1];
        dp[1] = dp[0] + dp[1];
        dp[0] = tmp;
        i++;
    }
    return dp[1];
}