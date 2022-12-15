def prime_factorize(N):
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p, e))
        print(res)
        print(N)
    print(N)
    if N != 1:
        
        res.append((N, 1))
    print(res)

    return res

if __name__ == "__main__":
    K=int(input())
    X=prime_factorize(K)
    ans=0
    # 素因数 x が num 個
    for x,num in X:
        rem=num
        # x ～ num*x の範囲に Nx は存在する
        for Nx in range(x,x*(num+1),x):
            j=Nx
            # jは何回 xで割れるか
            while j%x==0:
                j//=x
                rem-=1
                if rem<=0:
                    break
            if rem<=0:
                break

        ans=max(Nx,ans)

    print(ans)