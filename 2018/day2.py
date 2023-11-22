with open("2018/input2.txt") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

def part1(data):
    two = 0
    three = 0
    for i in data:
        seen = {}
        for j in i:
            if j in seen:
                seen[j] += 1
            else:
                seen[j] = 1
        if 2 in seen.values():
            two += 1
        if 3 in seen.values():
            three += 1
    return two * three

print(part1(data))

def part2(data):
    for i in data:
        for j in data:
            count = 0
            for k in range(len(i)):
                if i[k] != j[k]:
                    count += 1
            if count == 1:
                for k in range(len(i)):
                    if i[k] != j[k]:
                        return i[:k] + i[k+1:]

print(part2(data))