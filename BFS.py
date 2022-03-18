
tree = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'F'],
    'C' : ['G', 'H'],
    'D' : ['I', 'J'],
    'E' : ['K', 'L'],
    'F' : ['L', 'M'],
    'G' : ['N'],
    'H' : ['O', 'P'],
    'I' : ['P', 'Q'],
    'J' : ['R'],
    'K' : ['S'],
    'L' : ['T'],
    'P' : ['U']
}
start = 'A'
goal = 'U'


def BFS(s, g):
    open = []
    closed = []
    if s not in tree:
        return False
    open.append(s)

    while len(open) != 0:
        x = open.pop(0)
        if x == g:
            return True
        if not x in closed:
            print(x)
            closed.append(x)
            if x in tree:
                for val in tree[x]:
                    if val not in open:
                        open.append(val)
                
    return False

print(BFS(start, goal))