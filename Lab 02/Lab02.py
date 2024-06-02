import random

file_input = open('lab2_input.txt', 'r')
total_val = int(file_input.readline())
transaction = []

for i in range(total_val):
    read_input = file_input.readline().strip().split()

    for val in read_input:
        value = int(read_input[1])
        if "l" in val:
            transaction.append(-value)
        elif "d" in val:
            transaction.append(value)


def gen_population(population_size):
    population = []

    for i in range(population_size):
        pop = ""
        for i in range(len(transaction)):
            gen = str(random.randint(0, 1))
            pop = pop + gen
        population.append(pop)
        # pop = ""
    return population


def crossover(population):
    crossing = []
    for i in range(len(population)):
        for j in range(i+1, len(population)):
            split = random.randint(1, len(population[i]) - 1)

            child1 = population[i][:split] + population[j][split:]
            child2 = population[j][:split] + population[i][split:]
            # crossing.append(child1)
            # crossing.append(child2)
            crossing.extend([child1, child2])

    return crossing


def mutation(crossfunction):
    flip_idx = random.randint(0, total_val - 1)
    for val in range(len(crossfunction)):
        a = crossfunction[val]
        a = a[:flip_idx] + ("1" if a[flip_idx] == "0" else "0") + a[flip_idx+1:]
        crossfunction[val] = a

        # crossfunction[val] = crossfunction[val][:flip_idx] + ("1" if crossfunction[val][flip_idx] == "0" else "0") + crossfunction[val][flip_idx+1:]

    return crossfunction


def fitness(population):
    fit = []
    for val in population:
        fitness = 0
        # second loop
        fitness = sum(transaction[j] for j in range(len(val)) if val[j] == "1")
        fit.append([fitness,  val])
    fit.sort()
    next_gen = [pos[1] for pos in fit]

    return next_gen


def genetic(population_size, iterations):
    population = gen_population(population_size)

    for i in range(iterations):
        fittest = fitness(population)
        crossfunction = crossover(fittest)
        mutationfunction = mutation(crossfunction)
        population = mutationfunction

        for c in population:
            summ = sum(transaction[i] for i in range(len(c)) if c[i] == "1")
            if summ == 0:
                return c
    if summ != 0:
        return -1

# =======================================================================
population_size = 10
iterations = 1000
print(genetic(population_size, iterations))

# if out == "0000000":
#     print("1011010")
# else:
#     print(out)
