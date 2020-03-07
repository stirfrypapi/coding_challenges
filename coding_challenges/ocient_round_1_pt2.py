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


def generate_gene_sequence(lcg, length_gene):
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

    for i in range(num_pairs):
        num = generate_random_number(lcg)
        print(map_gene_pairs[num], end="")


if __name__ == "__main__":
    counter, length_gene = 0, 0
    num_terms, a, seed, c, m = 0, 48271, 0, 0, (2**32)-1
    for line in sys.stdin:
        if counter == 0:
            length_gene = int(line.strip())
        elif counter == 1:
            seed = int(line.strip())
        else:
            break
        counter += 1
    d = DataGenerator(a, seed, c, m, num_terms)
    generate_gene_sequence(d, length_gene)
