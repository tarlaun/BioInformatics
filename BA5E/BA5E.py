########################### BLOSUM READ #############################################
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

gap_score = -5  # indel penalty

# Read input
strings = open("input.txt", "r")
strings = (strings.read())
strings = strings.split("\n")
s0 = strings[0]
s1 = strings[1]
m = len(s0)
n = len(s1)
D = [[0 for i in range(m + 2)] for j in range(n + 2)]

# Initialization
D[0][0] = 0
for i in range(1, n + 1):
    D[i][0] = gap_score * i
for j in range(1, m + 1):
    D[0][j] = gap_score * j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        match = D[i - 1][j - 1] + blosum[letter_key[s0[j - 1]]][letter_key[s1[i - 1]]]
        gaps0 = D[i][j - 1] + gap_score
        gaps1 = D[i - 1][j] + gap_score
        D[i][j] = max(match, gaps0, gaps1)


# Backtrace
s0_aln = ""
s1_aln = ""
while i > 0 and j > 0:
    if D[i][j] - blosum[letter_key[s0[j - 1]]][letter_key[s1[i - 1]]] == D[i - 1][j - 1]:
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1
        j -= 1
    elif D[i][j] - gap_score == D[i][j - 1]:
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = '-' + s1_aln
        j -= 1
    elif D[i][j] - gap_score == D[i - 1][j]:
        s0_aln = '-' + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1

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

score = 0

print(D[n][m])
print(s0_aln)
print(s1_aln)

answer = open("answer.txt", "w")
answer.write(str(D[n][m]) + "\n")
answer.write(s0_aln + "\n")
answer.write(s1_aln)
answer.close()
