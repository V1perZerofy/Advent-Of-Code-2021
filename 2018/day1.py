with open("2018\input1.txt") as f:
    data = [int(line.strip()) for line in f.readlines()]
    f.close()

#part 1
def part1(data):
    return sum(data)

print(part1(data))

def part2(data):
    seen = set()
    freq = 0
    while True:
        for i in data:
            freq += i
            if freq in seen:
                return freq
            seen.add(freq)

print(part2(data))