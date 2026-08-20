'''D. Bermuda Rectangle
The Beaver is swimming across the ocean (yes, he can do that). Here, it aims to explore the Bermuda Rectangle. Of course, it poses no danger to The Beaver, but it is interesting from a scientific perspective.

Unlike the Bermuda Triangle, not much is known about the Bermuda Rectangle. Specifically, The Beaver knows for sure that the area of the rectangle is 𝑆, its sides are integers, and the bottom left corner is located at the point (0,0).

The Beaver is interested in how many cells from a rectangle with sides 𝑥 and 𝑦, whose bottom left corner is at the point (0,0), can be located within the Bermuda Rectangle. A cell is considered to be within the Bermuda Rectangle if there exists a rectangle that satisfies the given constraints of the Bermuda Rectangle and contains that cell. Help The Beaver quickly respond to queries! You need to answer 𝑞 such queries.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤10000). The description of the test cases follows.

The first line of each test case contains two integers 𝑆 and 𝑞 — the area of the Bermuda Rectangle and the number of queries (1≤𝑆≤1014; 1≤𝑞≤3⋅105).

This is followed by 𝑞 lines, each containing two integers 𝑥,𝑦 — the next query (1≤𝑥,𝑦≤𝑆).

It's guaranteed that the sum of 𝑞 over all test cases doesn't exceed 3⋅105.

It's guaranteed that the sum of 𝑆‾‾√ over all test cases doesn't exceed 107.

Output
For each query, output a single integer on a separate line — the answer to the query.
code:'''
from bisect import bisect_right
from math import isqrt


def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        S, q = map(int, input().split())

        # All possible widths of the Bermuda Rectangle
        divisors = []

        for d in range(1, isqrt(S) + 1):
            if S % d == 0:
                divisors.append(d)

                if d * d != S:
                    divisors.append(S // d)

        divisors.sort()

        # pref_w[i]  = total width of first i strips
        # pref_wh[i] = sum(width * height) of first i strips
        pref_w = [0]
        pref_wh = [0]

        previous = 0

        for a in divisors:
            b = S // a
            width = a - previous

            pref_w.append(pref_w[-1] + width)
            pref_wh.append(pref_wh[-1] + width * b)

            previous = a

        for _ in range(q):
            x, y = map(int, input().split())

            # Number of complete strips whose right edge <= x
            k = bisect_right(divisors, x)

            # Number of strips whose height >= y
            # S / a >= y  <=>  a <= S / y
            j = bisect_right(divisors, S // y)

            # Among the complete strips, these have height >= y.
            p = min(k, j)

            # Their contribution is simply width * y
            answer = y * pref_w[p]

            # Remaining complete strips have height < y,
            # so use their actual heights.
            if k > p:
                answer += pref_wh[k] - pref_wh[p]

            # There may be one final partial strip.
            if k < len(divisors):
                previous = divisors[k - 1] if k > 0 else 0

                width = x - previous
                height = S // divisors[k]

                answer += width * min(y, height)

            print(answer)


solve()
