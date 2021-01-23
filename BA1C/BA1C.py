def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


dna = open("input.txt", "r")
dna = (dna.read())
dna_split = dna.split("\n")
rc = reverse_complement(dna_split[0])
answer = open("answer.txt", "w")
answer.write(rc)
answer.close()
