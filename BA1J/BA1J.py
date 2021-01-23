import itertools

bases = ['A', 'T', 'G', 'C']


def create_kmers(k):
    return [''.join(p) for p in itertools.product(bases, repeat=k)]


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


dna = open("sample.txt", "r")
dna = (dna.read())
dna_split = dna.split("\n")
dna = dna_split[0]
splitted = dna_split[1].split(" ")
k = int(splitted[0])
d = int(splitted[1])
answer_str = ""
kmers = create_kmers(k)
max = 1
reverse = reverse_complement(dna)
for pattern in kmers:
    rc = reverse_complement(pattern)
    kmers.remove(rc)
    count = 0
    for i in range(len(dna) - len(pattern) + 1):
        sub = dna[i:i + len(pattern)]
        if hamming_distance(sub, pattern) <= d:
            count = count + 1
        if hamming_distance(sub, rc) <= d:
            count = count + 1

    if count == max:
        answer_str = answer_str + pattern + " "
        answer_str = answer_str + rc + " "
    if count > max:
        answer_str = ""
        answer_str = answer_str + pattern + " "
        answer_str = answer_str + rc + " "
        max = count

answer = open("answer.txt", "w")
answer.write(answer_str)
answer.close()
