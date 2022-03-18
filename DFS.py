
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


def DFS(s, g):
    open = []
    closed = []
    if s not in tree:
        return False
    open.append(s)

    while len(open) > 0:
        x = open.pop(0)
        # print("X = ",x)
        if x == g:
            return True
        if not x in closed:
            print(x)
            closed.append(x)
            if x in tree:
                tempList = []
                for val in tree[x]:
                    tempList.append(val)
                    # print("Added",val)
                open = tempList + open
                
    return False

print(DFS(start, goal))