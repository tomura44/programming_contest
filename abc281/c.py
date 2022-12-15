import bisect
from itertools import accumulate
n, t = [int(nt) for nt in input().split()]
a = [0] + [int(a) for a in input().split()]

t%=sum(a)

#累積和
aa = list(accumulate(a))

#bisectは値をソート済みのリストに挿入する位置のインデックスを返す
x = bisect.bisect_left(aa, t)
print(x, t-aa[x-1])