import disjoint_linked as dl

randoms = [random.randint(0, 999) for _ in range(33)]

# Create a disjoint set for each node
for i in randoms:
	dl.DisjointSetHandler().make_set(i)

