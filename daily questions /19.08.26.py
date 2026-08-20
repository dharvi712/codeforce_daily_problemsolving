'''A. Creating Abbreviations
The Beaver was given a set of words 𝑆, which initially contained 𝑛 words. Then he performed the following operation 𝑚 times:

The Beaver forms a sequence of one or more words from the set 𝑆. The same word may appear in the sequence several times. An abbreviation∗ is formed from the resulting phrase.
Then the Beaver adds the resulting abbreviation to 𝑆 and can now use it in subsequent operations as an ordinary word.
You are given the 𝑛 initial words that were in the set 𝑆, and the set of abbreviations that the Beaver formed. Determine whether the Beaver made a mistake and whether all these abbreviations could have appeared as a result of the operation described above. Note that the abbreviations did not necessarily appear in the same order in which they are given to you.

∗The abbreviation of a sequence is the word produced by the first letters of the words in the sequence. For example, the sequence birch OAK birch redwood produces the abbreviation BOBR.
Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤500). The description of the test cases follows.

The first line of each test case contains two integers 𝑛 and 𝑚 — the number of ordinary words and the number of abbreviations, respectively (1≤𝑛,𝑚≤100).

Each of the next 𝑛 lines contains one string 𝑤𝑖 — an ordinary word (1≤|𝑤𝑖|≤20).

Each of the next 𝑚 lines contains one string 𝑎𝑖 — an abbreviation formed by Bobr (1≤|𝑎𝑖|≤20).

All ordinary words consist of lowercase English letters, and all abbreviations consist of uppercase English letters. In each test case, all strings 𝑤1,𝑤2,…,𝑤𝑛,𝑎1,𝑎2,…,𝑎𝑚 are pairwise distinct.

The total length of all strings over all test cases does not exceed 50000.

Output
For each test case, print "YES" if there exists a suitable order in which the given abbreviations could have appeared, and "NO" otherwise.

You may print each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
code:'''
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx+1]); idx += 2
        words = []
        for _ in range(n):
            words.append(data[idx].decode()); idx += 1
        abbrs = []
        for _ in range(m):
            abbrs.append(data[idx].decode()); idx += 1

        available = [False]*26
        for w in words:
            available[ord(w[0].lower()) - ord('a')] = True

        letters_needed = []
        missing = [0]*m
        adj = [[] for _ in range(26)]

        for i, a in enumerate(abbrs):
            s = set(ord(c.lower()) - ord('a') for c in a)
            letters_needed.append(s)
            cnt = 0
            for L in s:
                if not available[L]:
                    cnt += 1
                    adj[L].append(i)
            missing[i] = cnt

        q = deque()
        created = [False]*m
        created_count = 0

        for i in range(m):
            if missing[i] == 0:
                q.append(i)

        while q:
            i = q.popleft()
            if created[i]:
                continue
            created[i] = True
            created_count += 1
            L = ord(abbrs[i][0].lower()) - ord('a')
            if not available[L]:
                available[L] = True
                for j in adj[L]:
                    if not created[j]:
                        missing[j] -= 1
                        if missing[j] == 0:
                            q.append(j)

        out.append("YES" if created_count == m else "NO")

    print("\n".join(out))

if __name__ == "__main__":
    main()
