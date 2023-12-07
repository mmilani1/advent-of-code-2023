input = "d01-input.txt"
input = open(input)

sum = 0
digits = '01234567689'
for line in input:
    p1, p2 = 0, len(line)-1

    while line[p1] not in digits:
        p1 += 1

    while line[p2] not in digits:
        p2 -= 1

    sum += int(line[p1]+line[p2])

print(sum)
