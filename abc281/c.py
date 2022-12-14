import bisect
from itertools import accumulate
n, t = [int(nt) for nt in input().split()]
a = [0] + [int(a) for a in input().split()]

t%=sum(a)

aa = list(accumulate(a))

x = bisect.bisect_left(aa, t)
print(x, t-aa[x-1])