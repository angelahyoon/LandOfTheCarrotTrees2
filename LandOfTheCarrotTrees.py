# -------------------- GRAPH - SETS / DICTIONARY ---------------------- #
class Graph:
    def __init__(self):
        # self.v = v
        self.graph = dict()
 
    def addEdge(self, a, b):
        if a not in self.graph:
            self.graph[a] = {b}
        else:
            self.graph[a].add(b)

        if b not in self.graph:
            self.graph[b] = {a}
        else:
            self.graph[b].add(a)

    def print_graph(self):
        for i, adjlist in sorted(self.graph.items()):
            print("Nodes with label ", i)
            for j in sorted(adjlist):
                      print(j)

# ----------------------------- STACK --------------------------------- #
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()

# ------------------------------ PREORDER ------------------------------- #
def preorder_traversal(G, r):
    visited = [r]
    stack = Stack()

    for c in G.graph.get(r):
        stack.push(c)

    stack.stack = sorted(stack.stack, reverse=True)

    while stack.isEmpty() == False:
        node = stack.pop()
        ch = sorted(G.graph.get(node), reverse=True)
        for c in ch:
            if c not in visited:
                stack.push(c)
        visited.append(node)

    return visited

# ----------------------------- OTHER FUNCTIONS --------------------------- #
def unique(l):
    unique_list = []
    for x in l:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# ------------------------------- INPUT ----------------------------------- #
data = input().split()
n, q = int(data[0]), int(data[1])

flavours = input().split()
unique_flavours = unique(flavours)
flavour_map = dict()
for i in range(n):
    node = i + 1
    flavour_map[str(node)] = flavours[i]

g = Graph()

for i in range(n-1):
    seq = input().split()
    g.addEdge(seq[0], seq[1])

# -------------------------------- SUBTREE ------------------------------- #
def subtree(node, graph, dict, tree):
    visited = [node]
    stack = Stack()

    flavours = []
    flavours.append(dict.get(node))

    children = sorted(graph.graph.get(node), reverse=True)

    for c in children:
        if tree.index(c) > tree.index(node):
            stack.push(c)

    stack.stack = sorted(stack.stack, reverse=True)

    while stack.isEmpty() == False:
        node = stack.pop()
        children = sorted(graph.graph.get(node), reverse=True)

        for child in children:
            if child not in visited:
                stack.push(child)
        visited.append(node)
        flavours.append(dict.get(node))
    return flavours

# -------------------------------- OUTPUT -------------------------------- #
while q:
    query = input().split()
    root, k = query[0], query[1]

    if int(k) == 1:
        print(n)
    elif int(k) > len(unique_flavours):
        print(0)
    else:
        count = 0
        tree = preorder_traversal(g, root)
        for node in tree:
            sub_flavours = unique(subtree(node, g, flavour_map, tree))
            # print("[" + ' '.join(str(x) for x in sub_flavours) + "]")
            # print(len(sub_flavours) >= int(k))
            if (len(sub_flavours) >= int(k)):
                count = count + 1
        print(count)
    q = q-1