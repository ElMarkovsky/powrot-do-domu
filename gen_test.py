# Program stworzony z wykorzystaniem SI
import sys
import random

if len(sys.argv) < 4:
    sys.exit("Uzycie: python3 gen_test.py <n> <m> <seed>")

n = int(sys.argv[1])
m = int(sys.argv[2])
seed = int(sys.argv[3])
random.seed(seed)

# 1. Liczba wierzchołków i krawędzi
print(f"{n} {m}")

# 2. Flagi miast (0 lub 1) dla każdego wierzchołka
for _ in range(n):
    print(random.choice([0, 1]))

# 3. Generowanie krawędzi
# Tworzymy losowe drzewo rozpinające, aby zagwarantować spójność grafu, a pozostałe krawędzie dociągamy losowo.
edges = set()

# Wstępne drzewo (n-1 krawędzi) zapewniające połączenie
nodes = list(range(n))
random.shuffle(nodes)
for i in range(1, n):
    u = nodes[i]
    v = random.choice(nodes[:i])
    if u > v:
        u, v = v, u
    edges.add((u, v))

# Dobieranie brakujących krawędzi do limitu m
while len(edges) < m:
    u = random.randint(0, n - 1)
    v = random.randint(0, n - 1)
    if u != v:
        if u > v:
            u, v = v, u
        edges.add((u, v))

# Wypisanie krawędzi z losową długością d (1 <= d <= 10000)
for u, v in edges:
    d = random.randint(1, 10000)
    print(f"{u} {v} {d}")

# 4. Losowy start i finish (start != finish)
start = random.randint(0, n - 1)
finish = random.randint(0, n - 1)
while finish == start:
    finish = random.randint(0, n - 1)

print(f"{start} {finish}")