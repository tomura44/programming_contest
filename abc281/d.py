N,K,D = map(int, input().split())
a = [int(a) for a in input().split()]
dp = [[[-1 for _ in range(K+1)] for _ in range(N+1)] for _ in range(D)]

dp[0][0][0] = 0

for n in range(N):
    for k in range(K+1):
        for d in range(D):
            if dp[d][n][k] >= 0:
                dp[d][n][k] = max(dp[d][n][k], dp[d][n+1][k])

                if k < K:
                    dp[(d + a[n]) % D][n + 1][k + 1] = max(dp[d][n][k] + a[n]), dp[(d+A[n], dp[(d+a[n])%D][n+1][k+1])]
                    
                    
if dp[0][-1][-1] >= 0:
    print(dp[0][-1][-1])
else:
    print(-1)