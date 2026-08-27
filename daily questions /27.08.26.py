import sys

input = sys.stdin.readline

t = int(input())

while t:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # We only care about the multiset of values.
    a.sort()
    b.sort()

    # Already equal -> zero operations.
    if a == b:
        print("YES")
        continue

    # x = XOR(a) XOR XOR(b)
    x = 0

    for v in a:
        x ^= v

    for v in b:
        x ^= v

    # We need x to be an element of a.
    idx = -1

    for i in range(n):
        if a[i] == x:
            idx = i
            break

    if idx == -1:
        print("NO")
        continue

    # Perform the operation using index idx.
    # IMPORTANT: skip ONLY idx.
    for i in range(n):
        if i != idx:
            a[i] ^= x

    # Order doesn't matter, so compare sorted arrays.
    a.sort()

    if a == b:
        print("YES")
    else:
        print("NO")
      '''2254 F. Whiplash
time limit per test2 seconds
memory limit per test256 megabytes
Yousef has given you an even integer 𝑛 and two arrays, 𝑎 and 𝑏, both consisting of 𝑛 non-negative integers.

You can perform the following operation on array 𝑎 any number of times (possibly zero):

Choose an index 𝑖 (1≤𝑖≤𝑛).
For all 𝑗 such that 1≤𝑗≤𝑛 and 𝑗≠𝑖, replace 𝑎𝑗 with 𝑎𝑗⊕𝑎𝑖. (Here, ⊕ denotes the bitwise XOR operation).
The element 𝑎𝑖 remains unchanged.
Determine whether it is possible to transform array 𝑎 into array 𝑏 using a finite number of operations.

Input
The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an even integer 𝑛 (2≤𝑛≤2⋅105) — the length of the array.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (0≤𝑎𝑖<230) — the elements of the array 𝑎.

The third line of each test case contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (0≤𝑏𝑖<230) — the elements of the array 𝑏.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case, output "YES" if the array 𝑎 can be transformed into array 𝑏 using a finite number of operations, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
inputCopy
6
2
1 2
1 0
4
1 2 4 7
6 7 5 3
4
1 2 4 8
8 4 2 1
4
1 2 3 4
1 2 4 5
4
1 2 0 3
3 3 0 3
6
3 5 6 9 10 12
6 5 3 12 15 9
outputCopy
NO
YES
YES
NO
NO
YES
Note
In the first test case, starting from [1,2], there is no sequence of operations that ends at [1,0], so the answer is "NO".

In the second test case, one valid sequence is:

Choose index 2, [1,2,4,7]→[3,2,6,5].
Choose index 3, [3,2,6,5]→[5,4,6,3].
Choose index 4, [5,4,6,3]→[6,7,5,3].
In the third test case, one valid sequence is:

Choose index 1, [1,2,4,8]→[1,3,5,9].
Choose index 2, [1,3,5,9]→[2,3,6,10].
Choose index 3, [2,3,6,10]→[4,5,6,12].
Choose index 2, [4,5,6,12]→[1,5,3,9].
Choose index 4, [1,5,3,9]→[8,12,10,9].
Choose index 1, [8,12,10,9]→[8,4,2,1].
      '''
      
