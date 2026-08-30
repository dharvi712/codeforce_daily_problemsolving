'''E. Chronostasis
time limit per test2 seconds
memory limit per test256 megabytes
Yousef has a hidden array 𝑎 of length 𝑛 consisting entirely of strictly positive integers.

An operation was performed exactly once to create an array 𝑏:

Set 𝑏1=𝑎1.
For every 𝑖 from 2 to 𝑛, set 𝑏𝑖=𝑎𝑖−𝑎𝑖−1.
After this, the elements of 𝑏 were completely shuffled.
You are given the shuffled array 𝑏. Reconstruct the lexicographically smallest original array 𝑎. If it's impossible for any arrangement of 𝑏 to produce an array 𝑎 of strictly positive integers, output −1.
,,
Input
The first line of input contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains an integer 𝑛 (1≤𝑛≤2⋅105) — the size of the array.

The second line of each test case contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (−109≤𝑏𝑖≤109) — the elements of the shuffled array 𝑏.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, output 𝑛 strictly positive integers 𝑎1,𝑎2,…,𝑎𝑛 (𝑎𝑖≥1) — the lexicographically smallest original array 𝑎. If it's impossible to create a valid array 𝑎, output −1 instead.

Example
inputCopy
8
1
5
4
-5 2 1 1
6
-3 4 2 -1 1 0
6
-2 -2 4 1 0 1
7
0 0 -2 3 0 -1 2
8
-1 -1 -1 -1 5 0 0 1
5
1000000000 500000000 750000000 100000000 900000000
10
1000000000 -1000000000 500000000 -500000000 1 1 -1 -1 2 -2
outputCopy
5 
-1
1 1 3 2 6 3 
1 1 2 6 4 2 
2 1 1 1 1 4 2 
1 1 1 6 5 4 3 2 
100000000 600000000 1350000000 2250000000 3250000000 
-1
Note
In the first test case, the only valid array is 𝑎=[5].

In the second test case, there is no valid arrangement of the elements of 𝑏 that reconstructs an array 𝑎 consisting entirely of strictly positive integers. Therefore, the answer is −1.

In the third test case, one valid arrangement reconstructs the array 𝑎=[1,1,3,2,6,3]. The resulting sequence of differences [1,0,2,−1,4,−3] is a permutation 
of the given array 𝑏, and among alfrom bisect import bisect_right'''

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        """
        Return the smallest index whose prefix sum >= k.
        """
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)

        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1

        return idx + 1


class Solution:
    def solve(self):
        import sys
        input = sys.stdin.readline

        t = int(input())

        for _ in range(t):
            n = int(input())
            b = list(map(int, input().split()))

            # The final prefix sum is sum(b) = a[n].
            # It must be positive.
            if sum(b) <= 0:
                print(-1)
                continue

            # Coordinate compression
            vals = sorted(set(b))
            m = len(vals)

            fw = Fenwick(m)

            # Frequency of every value
            for x in b:
                idx = bisect_right(vals, x)
                fw.add(idx, 1)

            cur = 0
            ans = []
            possible = True

            for _ in range(n):
                # Need:
                # cur + x > 0
                # => x > -cur
                #
                # Since values are integers:
                # x >= -cur + 1
                pos = bisect_right(vals, -cur)

                # No value > -cur exists
                if pos >= m:
                    possible = False
                    break

                # Number of elements <= -cur
                before = fw.sum(pos)

                # Find the first remaining element after that.
                total_remaining = fw.sum(m)

                if before == total_remaining:
                    possible = False
                    break

                idx = fw.kth(before + 1)
                x = vals[idx - 1]

                # Remove x
                fw.add(idx, -1)

                cur += x
                ans.append(cur)

            if possible and cur > 0:
                print(*ans)
            else:
                print(-1)l valid reconstructions, this array is lexicographically smallest.'''



