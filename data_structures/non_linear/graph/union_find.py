def make_set(vertex_count):
	return [x for x in range(vertex_count)]


class UnionFind:
	def __init__(self, vertex_count):
		self.parent = make_set(vertex_count)
		self.rank = [1] * vertex_count
		self.count = vertex_count

	def union(self, x, y):
		root1 = self.find(x)
		root2 = self.find(y)

		if root1 == root2:
			return
		elif self.rank[root1] > self.rank[root2]:
			self.parent[root2] = self.parent[root1]
			self.rank[root1] += 1
		else:
			self.parent[root1] = self.parent[root2]
			self.rank[root2] += 1
		self.count -= 1

	def find(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

def main():
	edges = [
		[0, 2],
		[1, 4],
		[1, 5],
		[2, 3],
		[2, 7],
		[4, 8],
		[5, 8]
	]

	number_of_edges = 9
	union_find = UnionFind(number_of_edges)

	for vertex1, vertex2 in edges:
		union_find.union(vertex1, vertex2)

	print(f"Number of Connected Components is {union_find.count}.")

if __name__ == "__main__":
	main()

