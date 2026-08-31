MOD = 998244353

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = 1

    # Check odd positions and even positions separately
    for start in range(2):
        ways = 0

        # Pattern 0,1,0,1,...
        ok = True
        for i in range(start, n, 2):
            expected = (i - start) // 2 % 2
            if s[i] != '?' and int(s[i]) != expected:
                ok = False
                break

        if ok:
            ways += 1

        # Pattern 1,0,1,0,...
        ok = True
        for i in range(start, n, 2):
            expected = 1 - ((i - start) // 2 % 2)
            if s[i] != '?' and int(s[i]) != expected:
                ok = False
                break

        if ok:
            ways += 1

        ans = ans * ways % MOD

    print(ans)
  '''2256B.B. Domino Tiles
time limit per test1 second
memory limit per test256 megabytes
Nygglatho returns from the market with an old box of tiles whose painted marks have begun to fade. Before she can put it away, Chtholly and the young fairies have already spread the tiles across the dining table and turned them into a puzzle.

There is a row of 𝑛 tiles. Each tile should be marked with either 𝟶 or 𝟷. However, some of the marks have faded away.

The current row is represented by a string 𝑠 of length 𝑛. Each character of 𝑠 is 𝟶, 𝟷, or ?. Chtholly must replace every ? with either 𝟶 or 𝟷.

After replacement, for every 1≤𝑖<𝑛, the two neighboring tiles 𝑠𝑖 and 𝑠𝑖+1 form a domino of weight (𝑠𝑖+𝑠𝑖+1). Note that two consecutive dominoes share exactly one tile. The completed row is valid if every two consecutive dominoes have different weights.

Determine the number of different∗ ways to replace all ? characters so that the completed row is valid. Output the answer modulo 998244353.

∗Two ways of replacement are considered different if the resulting strings are different.
Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤104). The description of the test cases follows.

The first line of each test case contains one integer 𝑛 (2≤𝑛≤2⋅105) — the number of tiles.

The second line contains the string 𝑠 of length 𝑛, where 𝑠𝑖=𝟶, 𝟷, or ?.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, output one integer — the number of valid ways to replace all ? characters, modulo 998244353.

Example
inputCopy
4
2
??
5
0?1??
5
0?0??
8
00110011
outputCopy
4
2
0
1
Note
In the first test case, there is only one domino, so every completion is valid. The valid completed strings are 𝟶𝟶, 𝟶𝟷, 𝟷𝟶, and 𝟷𝟷.

In the second test case, the valid completed strings are 𝟶𝟶𝟷𝟷𝟶 and 𝟶𝟷𝟷𝟶𝟶.

In the third test case, there are no valid completed strings.

In the fourth test case, the only valid completed string is 𝟶𝟶𝟷𝟷𝟶𝟶𝟷𝟷.'''
