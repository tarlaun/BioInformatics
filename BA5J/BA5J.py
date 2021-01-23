########################### READ BLOSUM #############################################
blosum62 = open("blosum62.txt", "r")
blosum62 = (blosum62.read())
blosum62_lines = blosum62.split("\n")

blosum = [[0 for x in range(20)] for y in range(20)]
letter_key = dict()
i = 0

letters = blosum62_lines[0].split()
for c in letters:
    letter_key[c] = i
    i += 1

for i in range(1, 21):
    line = blosum62_lines[i].split()
    for j in range(1, 21):
        blosum[i - 1][j - 1] = int(line[j])

########################### BLOSUM READ #############################################
gap_start = -11  # indel penalty
gap_extend = -1

# Read input
strings = open("input.txt", "r")
strings = (strings.read())
strings = strings.split("\n")
s0 = strings[0]
s1 = strings[1]
m = len(s0)
n = len(s1)
M = [[0 for i in range(m + 2)] for j in range(n + 2)]
X = [[0 for i in range(m + 2)] for j in range(n + 2)]
Y = [[0 for i in range(m + 2)] for j in range(n + 2)]

# Initialization

for i in range(0, n + 1):
    M[i][0] = -10000
for j in range(0, m + 1):
    M[0][j] = -10000

for i in range(0, n + 1):
    X[i][0] = -10000

for j in range(0, m + 1):
    X[0][j] = gap_start + ((j-1) * gap_extend)

for i in range(0, n + 1):
    Y[i][0] = gap_start + ((i-1) * gap_extend)

for j in range(0, m + 1):
    Y[0][j] = -10000

M[0][0] = 0
X[0][0] = 0
Y[0][0] = 0
m_prev = [[0 for i in range(m + 2)] for j in range(n + 2)]
x_prev = [[0 for i in range(m + 2)] for j in range(n + 2)]
y_prev = [[0 for i in range(m + 2)] for j in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):

        max_x = max(gap_extend + X[i][j - 1], gap_start + M[i][j - 1],
                      gap_start + Y[i][j - 1])
        X[i][j] = max_x
        if max_x == gap_start + M[i][j - 1]:
            x_prev[i][j] = 'M'
        elif max_x == gap_extend + X[i][j - 1]:
            x_prev[i][j] = 'X'
        elif max_x == gap_start + Y[i][j - 1]:
            x_prev[i][j] = 'Y'

        max_y = max(gap_extend + Y[i - 1][j], gap_start + M[i - 1][j],
                      gap_start + X[i - 1][j])
        Y[i][j] = max_y
        if max_y == gap_start + M[i - 1][j]:
            y_prev[i][j] = 'M'
        elif max_y == gap_start + X[i - 1][j]:
            y_prev[i][j] = 'X'
        elif max_y == gap_extend + Y[i - 1][j]:
            y_prev[i][j] = 'Y'

        max_m = max(M[i - 1][j - 1], Y[i - 1][j - 1], X[i - 1][j - 1])
        M[i][j] = blosum[letter_key[s0[j - 1]]][letter_key[s1[i - 1]]] + max_m
        if max_m == M[i - 1][j - 1]:
            m_prev[i][j] = 'M'
        elif max_m == X[i - 1][j - 1]:
            m_prev[i][j] = 'X'
        elif max_m == Y[i - 1][j - 1]:
            m_prev[i][j] = 'Y'

# Backtrace
s0_aln = ""
s1_aln = ""
max_score = max(M[n][m], X[n][m], Y[n][m])
if max_score == M[n][m]:
    state = 'M'
elif max_score == X[n][m]:
    state = 'X'
elif max_score == 'Y':
    state = 'Y'

while i>0 and j>0:

    if state == 'M':
        prev = m_prev[i][j]
    elif state == 'X':
        prev = x_prev[i][j]
    elif state == 'Y':
        prev = y_prev[i][j]

    if state == 'M':
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1
        j -= 1
    elif state == 'Y':
        s0_aln = '-' + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1
    elif state == 'X':
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = '-' + s1_aln
        j -= 1
    state = prev

# Complete strings
if j > 0:
    while j > 0:
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = '-' + s1_aln
        j -= 1
elif i > 0:
    while i > 0:
        s1_aln = s1[i - 1] + s1_aln
        s0_aln = '-' + s0_aln
        i -= 1

ans = max(M[n][m], X[n][m], Y[n][m])

answer = open("answer.txt", "w")
answer.write(str(ans) + "\n")
answer.write(s0_aln + "\n")
answer.write(s1_aln)
answer.close()
