# n-gon
Number of ways to color edges of a n-gon using c colors allowing only rotations

Some Results:
```
EDGES: 2 COLORS: 1   Different Stones: 1
EDGES: 2 COLORS: 2   Different Stones: 3
EDGES: 2 COLORS: 3   Different Stones: 6
EDGES: 2 COLORS: 4   Different Stones: 10
EDGES: 2 COLORS: 5   Different Stones: 15
EDGES: 2 COLORS: 6   Different Stones: 21
EDGES: 2 COLORS: 7   Different Stones: 28
EDGES: 2 COLORS: 8   Different Stones: 36
EDGES: 2 COLORS: 9   Different Stones: 45
EDGES: 2 COLORS: 10   Different Stones: 55

EDGES: 3 COLORS: 1   Different Stones: 1
EDGES: 3 COLORS: 2   Different Stones: 4
EDGES: 3 COLORS: 3   Different Stones: 11
EDGES: 3 COLORS: 4   Different Stones: 24
EDGES: 3 COLORS: 5   Different Stones: 45
EDGES: 3 COLORS: 6   Different Stones: 76
EDGES: 3 COLORS: 7   Different Stones: 119
EDGES: 3 COLORS: 8   Different Stones: 176
EDGES: 3 COLORS: 9   Different Stones: 249
EDGES: 3 COLORS: 10   Different Stones: 340

EDGES: 4 COLORS: 1   Different Stones: 1
EDGES: 4 COLORS: 2   Different Stones: 6
EDGES: 4 COLORS: 3   Different Stones: 24
EDGES: 4 COLORS: 4   Different Stones: 70
EDGES: 4 COLORS: 5   Different Stones: 165
EDGES: 4 COLORS: 6   Different Stones: 336
EDGES: 4 COLORS: 7   Different Stones: 616
EDGES: 4 COLORS: 8   Different Stones: 1044
EDGES: 4 COLORS: 9   Different Stones: 1665
EDGES: 4 COLORS: 10   Different Stones: 2530


N    | OEIS Sequence | Formula
------------------------------------
2       A000217    a(n) = n*(n+1)/2
3       A006527    a(n) = (n^3 + 2*n)/3
4       A006528    a(n) = (n^4 + n^2 + 2*n)/4
5       A054620    a(n) = (n^5+4*n)/5
6       A006565    a(n) = (n^6+n^3+2*n^2+2*n)/6
7       A054621    a(n) = (n^7 + 6*n)/7  
8       A054622    a(n) = Sum_{d|8} phi(d)*n^(8/d)/8 = n*(n+1)*(n^6-n^5+n^4-n^3+2*n^2-2*n+4)/8
9       A054623    a(n) = n*(n^8+2*n^2+6)/9
10      A054624    a(n) = n*(n+1)*(n^8-n^7+n^6-n^5+n^4+4)/10
```

E.g.: “Number of ways to color vertices of a heptagon using <= n colors, allowing only rotations.”

One Formula for all: A075195
„Jablonski table T(n,k) read by antidiagonals: T(n,k) = number of necklaces with n beads of k colors.”
