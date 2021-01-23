dna = open("input.txt", "r")
dna = (dna.read())
dna_split = dna.split("\n")
pattern = dna_split[0]
dna = dna_split[1]


def find_all(dna, pattern):
    start = 0
    while True:
        start = dna.find(pattern, start)
        if start == -1: return
        yield start
        start += 1


answer_str = ""
for i in list(find_all(dna, pattern)):
    answer_str = answer_str + str(i)
    answer_str = answer_str + " "

answer = open("answer.txt", "w")
answer.write(answer_str)
answer.close()
