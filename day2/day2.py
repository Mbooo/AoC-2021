import time
data = []
start = time.time()
with open("input.txt","r") as file:
    for line in file:
        data.append(line.split())

def part1():
    horizontal, depth = 0,0

    for i in data:
        if i[0] == 'forward':
            horizontal += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        else:
            depth -= int(i[1])
    print("Partie 1 : ",horizontal * depth)


def part2():
    aim, horizontal, depth = 0, 0, 0
    for i in data:
        if i[0] == 'forward':
            horizontal += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        else:
            aim -= int(i[1])
    print("Partie 2 : ", horizontal * depth)



end = time.time()
part1()
part2()
elapsed = end - start
print(f"Temps d'éxecution : {elapsed:.2}ms")