import random
import disjoint_linked as dl

n = 10
randoms = [random.randint(0, 999) for _ in range(n)]

# Create a SINGLE instance of DisjointSetHandler
handler = dl.DisjointSetHandler()

# Create a disjoint set for each node
for i in randoms:
    handler.make_set(i)

# Union every set to the first set
for i in range(0, n-1):
	handler.print()
	j = random.randrange(1, n-i)
	handler.union(0, j)

# Print all sets
handler.print()
