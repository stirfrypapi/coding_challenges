import random
import sys


class DataGenerator:
    def __init__(self, a, X_0, c, m, num_terms):
        self.a = a
        self.seed = X_0
        self.c = c
        self.m = m
        self.num_terms = num_terms
        self.current = self.seed

    def generate_next_number(self):
        self.current = (self.a * self.current + self.c) % self.m

    def print_current(self):
        print(self.current, end=" ")

    def generate_all_terms(self):
        for i in range(0, self.num_terms):
            self.print_current()
            self.generate_next_number()


def generate_random_number(lcg):
    lcg.generate_next_number()
    x = lcg.current
    while x > lcg.m - (lcg.m % 100):
        lcg.generate_next_number()
        x = lcg.current
    return x % 100


def is_mutation(mutation_prob):
    first_num = int((mutation_prob / 2) * 99)
    second_num = int(((1 - mutation_prob) / 2) * 99)

    random_num = random.randint(0, first_num+second_num-1)

    return random_num < first_num


def swap_nucleotides(gene_pair):
    return gene_pair[::-1]


def transpose(gene_pair, genome):
    count = random.randint(0, 99)
    if count == 0:
        return genome + gene_pair
    return genome[:-count] + gene_pair + genome[-count:]


def duplication(gene_pair):
    count = random.randint(0, 9) + 1
    return gene_pair + gene_pair * count


def deletion(gene_pair):
    return ""


def generate_gene_sequence(lcg, length_gene, mutation_prob):
    map_gene_pairs = ["XX" for _ in range(100)]
    for i in range(0, 100):
        if i <= 5:
            map_gene_pairs[i] = "aa"
        elif i <= 14:
            map_gene_pairs[i] = "at"
        elif i <= 21:
            map_gene_pairs[i] = "ac"
        elif i <= 24:
            map_gene_pairs[i] = "ag"
        elif i <= 28:
            map_gene_pairs[i] = "ta"
        elif i <= 32:
            map_gene_pairs[i] = "tt"
        elif i <= 42:
            map_gene_pairs[i] = "tc"
        elif i <= 54:
            map_gene_pairs[i] = "tg"
        elif i <= 66:
            map_gene_pairs[i] = "ca"
        elif i <= 68:
            map_gene_pairs[i] = "ct"
        elif i <= 73:
            map_gene_pairs[i] = "cc"
        elif i <= 78:
            map_gene_pairs[i] = "cg"
        elif i <= 85:
            map_gene_pairs[i] = "ga"
        elif i <= 96:
            map_gene_pairs[i] = "gt"
        elif i <= 97:
            map_gene_pairs[i] = "gc"
        else:
            map_gene_pairs[i] = "gg"

    num_pairs = int(length_gene / 2)

    genome = ""
    for i in range(num_pairs):
        num = generate_random_number(lcg)
        gene_pair = map_gene_pairs[num]

        if is_mutation(mutation_prob):
            mutation_type = random.randint(0, 3)

            if mutation_type == 0:
                gene_pair = swap_nucleotides(gene_pair)
                genome += gene_pair
            elif mutation_type == 1:
                genome = transpose(gene_pair, genome)
            elif mutation_type == 2:
                gene_pair = duplication(gene_pair)
                genome += gene_pair
            elif mutation_type == 3:
                gene_pair = deletion(gene_pair)
                genome += gene_pair
        else:
            genome += gene_pair

    return genome


class Organism:
    def __init__(self, species, genome):
        self.species = species
        self.genome = genome


if __name__ == "__main__":
    # stdin counter
    counter = 0

    # random number generator
    num_terms, a, seed, c, m = 0, 48271, 0, 0, (2**32)-1

    # organism
    genome_length, mutation_prob = 0, 0

    for line in sys.stdin:
        if counter == 0:
            seed = int(line.strip())
        elif counter == 1:
            genome_length = int(line.strip())
        elif counter == 2:
            mutation_prob = float(line.strip())
        else:
            break
        counter += 1

    random.seed(seed)

    d = DataGenerator(a, seed, c, m, num_terms)

    genome = generate_gene_sequence(d, genome_length, mutation_prob)

    animal = Organism(seed, genome)

    print(animal.genome)