import time
start = time.time()
depths = []
with open("input.txt", "r") as file:
    for line in file:
        data = line.strip()
        depths.append(int(data))

def part1():
    increases = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            increases += 1
    print("Nombre de mesure supérieure à la précédente : ",increases)

def part2():
    #sums = []
    sumIncreases = 0
    # for i in range(len(depths) - 2):
    #     sums.append(depths[i] + depths[i+1] + depths[i+2])
    # for j in range(len(sums) - 1):
    #     if sums[j] < sums[j+1]:
    #         sumIncreases += 1
    for i in range(len(depths) - 3):
        if depths[i] < depths[i+3]:
            sumIncreases += 1

    print("Nombre de sommes de triplet supérieure à la précédente : ", sumIncreases)


part1()
part2()
end = time.time()
elapsed = end - start

print(f"Temps d'éxecution : {elapsed : .2}ms")