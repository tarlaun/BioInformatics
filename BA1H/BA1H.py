def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))



input = open("input.txt", "r")
input = (input.read())
splitted = input.split("\n")

pattern = splitted[0]
dna = splitted[1]
d = int(splitted[2])
answer_str = ""
for i in range(len(dna) - len(pattern)):
    sub = dna[i:i + len(pattern)]
    if hamming_distance(sub, pattern) <= d:
        answer_str = answer_str + str(i) + " "

answer = open("answer.txt", "w")
answer.write(answer_str)
answer.close()
