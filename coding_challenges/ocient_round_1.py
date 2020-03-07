import sys

class DataGenerator:
    def __init__(self, a, X_0, c, m, num_terms):
        self.a = a
        self.seed = X_0
        self.c = c
        self.m = m
        self.num_terms = num_terms
        self.current = (self.a * self.seed + self.c) % self.m
        self.generate_all_terms()

    def generate_next_number(self):
        self.current = (self.a * self.current + self.c) % self.m

    def print_current(self):
        print(self.current, end=" ")

    def generate_all_terms(self):
        for i in range(0, self.num_terms):
            self.print_current()
            self.generate_next_number()

if __name__ == "__main__":
    counter = 0
    num_terms, a, seed, c, m = 0, 0, 0, 0, 0
    for line in sys.stdin:
        if counter == 0:
            num_terms = int(line.strip())
        elif counter == 1:
            a = int(line.strip())
        elif counter == 2:
            seed = int(line.strip())
        elif counter == 3:
            c = int(line.strip())
        elif counter == 4:
            m = int(line.strip())
        else:
            break
        counter += 1
    d = DataGenerator(a, seed, c, m, num_terms)
