def longest_common_subsequence(s1: str, s2: str) -> int:
    s1 = "0" + s1
    s2 = "0" + s2
    m, n = len(s1), len(s2)

    dp = [[0] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
