B. A Ribbon for Tomorrow
time limit per test2 seconds
memory limit per test256 megabytes

Nephren has never been fond of long farewells. Before Chtholly leaves for her next mission, she says nothing and begins preparing a small ribbon for her instead.

She places n
 glass beads in a row on the table before threading them onto the ribbon. Each bead is either white or black. A binary∗
 string s
 represents their colors: the character 0
 represents a white bead, and the character 1
 represents a black bead.

To make the arrangement less ordinary, Nephren turns it into a small game. She can perform the following operation any number of times (possibly zero):

Choose two indices l
 and r
 (1≤l≤r≤n
) such that sl=sr
 in the current string, and reverse†
 the substring slsl+1…sr
.
For example, if s=00110
, Nephren may choose l=1
 and r=5
, since s1=s5=0
. After the operation, the string becomes 01100
.

Determine the number of different binary strings that can be obtained from s
. Since this number may be large, output it modulo 998244353
.

∗
A binary string is a string where each character is either 0
 or 1
.

†
To reverse a substring slsl+1…sr
 means to replace it with srsr−1…sl
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains one integer n
 (1≤n≤106
) — the number of beads.

The second line contains a binary string s
 of length n
, describing the colors of the beads.

It is guaranteed that the sum of n
 over all test cases does not exceed 106
.

Output
For each test case, output a single integer — the number of different binary strings that can be obtained from s
, modulo 998244353
.

Example
InputCopy
4
5
00110
6
001010
5
01010
6
111111
OutputCopy
2
3
1
1
Note
In the first test case, exactly the following two strings can be obtained:

00110
;
01100
.
For example, reversing the entire string 00110
 produces 01100
.

In the second test case, exactly the following three strings can be obtained:

001010
;
010010
;
010100
.
For example, 010010
 can be obtained by reversing the first four characters of 001010
, and 010100
 can be obtained by reversing the entire string 001010
.

In the third test case, every substring whose endpoints contain the same character is a palindrome. Therefore, reversing any valid substring does not change the string, and only 01010
 can be obtained.

In the fourth test case, we can only get 111111
.


import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    MOD = 998244353

    MAXN = 10**6 + 10
    fact = [1] * MAXN
    for i in range(1, MAXN):
        fact[i] = fact[i-1] * i % MOD
    inv = [1] * MAXN
    inv[MAXN-1] = pow(fact[MAXN-1], MOD-2, MOD)
    for i in range(MAXN-1, 0, -1):
        inv[i-1] = inv[i] * i % MOD

    def C(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv[r] % MOD * inv[n-r] % MOD

    out = []
    pos = 1
    for _ in range(t):
        n = int(data[pos]); pos += 1
        s = data[pos].decode(); pos += 1

        c0 = s.count('0')
        c1 = n - c0

        # blocks = 1 + number of adjacent transitions
        k = 1 + s.count('01') + s.count('10')

        if s[0] == '0':
            b0 = (k + 1) // 2
            b1 = k // 2
        else:
            b1 = (k + 1) // 2
            b0 = k // 2

        a = C(c0 - 1, b0 - 1) if c0 else 1
        b = C(c1 - 1, b1 - 1) if c1 else 1
        out.append(a * b % MOD)

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()
