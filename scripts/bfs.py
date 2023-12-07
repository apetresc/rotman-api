def bft(g, root):
  seen = set()
  q = [root]

  while q:
    n = q.pop(0)
    if n not in seen:
      print(n)
      seen.add(n)
      q += g[n]


GRAPH = {
  'A': ['B', 'D', 'E'],
  'B': ['C', 'D'],
  'C': [],
  'D': ['A', 'C', 'E'],
  'E': [],
  'F': ['G'],
  'G': ['D']
}

ROOT_NODE = 'F'


if __name__ == "__main__":
  bft(GRAPH, ROOT_NODE)
