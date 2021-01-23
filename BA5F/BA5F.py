########################### READ SCORING MATRIX #############################################
pam250 = open("pam250.txt", "r")
pam250 = (pam250.read())
pam250_lines = pam250.split("\n")

pam = [[0 for x in range(20)] for y in range(20)]
letter_key = dict()
i = 0

letters = pam250_lines[0].split()
for c in letters:
    letter_key[c] = i
    i += 1

for i in range(1, 21):
    line = pam250_lines[i].split()
    for j in range(1, 21):
        pam[i - 1][j - 1] = int(line[j])

########################### SCORING MATRIX READ #############################################
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
    D[i][0] = 0
for j in range(1, m + 1):
    D[0][j] = 0

max_d = -1
max_i = 0
max_j = 0
prev = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        match = D[i - 1][j - 1] + pam[letter_key[s0[j - 1]]][letter_key[s1[i - 1]]]
        gaps0 = D[i][j - 1] + gap_score
        gaps1 = D[i - 1][j] + gap_score
        D[i][j] = max(match, gaps0, gaps1, 0)
        if D[i][j] >= max_d:
            max_d = D[i][j]
            max_i = i
            max_j = j
        if D[i][j] == match:
            prev[i][j] = 'MATCH'
        elif D[i][j] == gaps0:
            prev[i][j] = 'GAPS0'
        elif D[i][j] == gaps1:
            prev[i][j] = 'GAPS1'
        else:
            prev[i][j] = 'STOP'

i = max_i
j = max_j

# Traceback
s0_aln = ""
s1_aln = ""
while D[i][j] > 0:
    if prev[i][j] == 'MATCH':
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1
        j -= 1

    elif prev[i][j] == 'GAPS1':
        s0_aln = '-' + s0_aln
        s1_aln = s1[i - 1] + s1_aln
        i -= 1
    elif prev[i][j] == 'GAPS0':
        s0_aln = s0[j - 1] + s0_aln
        s1_aln = '-' + s1_aln
        j -= 1

    else:
        i = 0
        j = 0



answer = open("answer.txt", "w")
answer.write(str(D[max_i][max_j]) + "\n")
answer.write(s0_aln + "\n")
answer.write(s1_aln)
answer.close()
