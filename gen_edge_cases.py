# Stworzone z wykorzystaniem SI
import sys
import random

def make_int_overflow():
    """Test 1: Przepełnienie 32-bitowego int.
    Łańcuch 40 000 wierzchołków miasto-miasto po 10 000 km.
    Koszt: 40 000 * 800 000 ml = 3.2 * 10^10 ml (wykracza poza zakres int32).
    """
    n = 40000
    m = n - 1
    print(f"{n} {m}")
    for _ in range(n):
        print(1)
    for i in range(m):
        print(f"{i} {i + 1} 10000")
    print(f"0 {n - 1}")

def make_no_path():
    """Test 2: Brak połączenia (graf niespójny).
    Dwie odrębne składowe po 500 wierzchołków bez krawędzi łączącej.
    Oczekiwane wyjście: -1 w obu liniach.
    """
    n = 1000
    m = n - 2
    print(f"{n} {m}")
    for _ in range(n):
        print(0)
    # Składowa 1: 0 .. 499
    for i in range(499):
        print(f"{i} {i + 1} 10")
    # Składowa 2: 500 .. 999
    for i in range(500, 999):
        print(f"{i} {i + 1} 10")
    print(f"0 {n - 1}")

def make_sub_liter():
    """Test 3: Spalanie poniżej 1 litra (zaokrąglanie w dół).
    Pojedynczy odcinek wiejski 5 km -> 250 ml -> 0 pełnych litrów.
    """
    print("2 1")
    print("0\n0")
    print("0 1 5")
    print("0 1")

def make_dense_stress():
    """Test 4: Duży graf wielokrotny / test wydajnościowy dla kolejki.
    Maksymalne limity N=100 000, M=300 000 z wieloma alternatywnymi drogami.
    Wymusza optymalne O(M log N) i odsiewanie nieaktualnych wpisów z kolejki.
    """
    random.seed(42)
    n = 100000
    m = 300000
    print(f"{n} {m}")
    for _ in range(n):
        print(random.choice([0, 1]))

    edges = set()
    # Zapewnienie głównego kręgosłupa
    for i in range(n - 1):
        edges.add((i, i + 1))

    # Dołożenie krawędzi do 300 000 o małych rozstępach indeksów
    while len(edges) < m:
        u = random.randint(0, n - 1)
        step = random.choice([2, 3, 5, 10])
        v = u + step
        if v < n:
            edges.add((u, v))
        else:
            v = max(0, u - step)
            if u != v:
                edges.add((min(u, v), max(u, v)))

    for u, v in edges:
        d = random.randint(1, 100)
        print(f"{u} {v} {d}")

    print(f"0 {n - 1}")

def make_city_vs_country():
    """Test 5: Pułapka na BFS / algorytmy liczące kroki.
    Trasa bezpośrednia przez miasto: 1 krawędź, 100 km * 80 ml = 8000 ml.
    Trasa objazdowa wiejska: 3 krawędzie, 3 * 40 km * 50 ml = 6000 ml.
    Poprawny algorytm wybierze dłuższą trasę o mniejszym spalaniu.
    """
    print("5 4")
    print("1")  # wierzchołek 0 (start, miasto)
    print("1")  # wierzchołek 1 (cel, miasto)
    print("0")  # wierzchołek 2 (wieś)
    print("0")  # wierzchołek 3 (wieś)
    print("0")  # wierzchołek 4 (wieś)
    # Krawędź bezpośrednia (droga)
    print("0 1 100")
    # Objazd wiejski (tańszy)
    print("0 2 40")
    print("2 3 40")
    print("3 1 40")
    print("0 1")

if __name__ == "__main__":
    case = sys.argv[1] if len(sys.argv) > 1 else ""
    if case == "overflow":
        make_int_overflow()
    elif case == "nopath":
        make_no_path()
    elif case == "subliter":
        make_sub_liter()
    elif case == "stress":
        make_dense_stress()
    elif case == "city_vs_country":
        make_city_vs_country()
    else:
        sys.exit("Uzycie: python3 gen_edge_cases.py [overflow|nopath|subliter|stress|city_vs_country]")