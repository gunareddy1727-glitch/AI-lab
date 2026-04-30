import heapq

GOAL_STATE = [[1,2,3],[4,5,6],[7,8,0]]

class EightPuzzle:

    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    # check goal state
    def is_goal_state(self):
        return self.state == GOAL_STATE

    # display board
    def display_state(self):
        for row in self.state:
            print(row)
        print()

    # find blank tile
    def find_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    # generate successor states
    def generate_successors(self):
        x, y = self.find_blank_position()
        successors = []

        moves = [("Up",-1,0),("Down",1,0),("Left",0,-1),("Right",0,1)]

        for name, dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                successors.append(EightPuzzle(new_state, self, name, self.depth+1))

        return successors


# heuristic (Manhattan Distance)
def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                dist += abs(x-i) + abs(y-j)
    return dist


# A* search algorithm
def a_star_search(start_node):
    pq = []
    visited = set()

    heapq.heappush(pq, (manhattan_distance(start_node.state), id(start_node), start_node))

    while pq:
        _, _, current = heapq.heappop(pq)

        if current.is_goal_state():
            return current

        visited.add(str(current.state))

        for child in current.generate_successors():
            if str(child.state) not in visited:
                cost = child.depth + manhattan_distance(child.state)
                heapq.heappush(pq, (cost, id(child), child))


# ---- RUN ----
initial_state = [[1,2,3],[4,0,6],[7,5,8]]
start = EightPuzzle(initial_state)

goal_node = a_star_search(start)

# trace solution path
path = []
while goal_node:
    path.append(goal_node)
    goal_node = goal_node.parent
path.reverse()

# print steps
for i, node in enumerate(path):
    print("Step", i)
    node.display_state()
    if node.move:
        print("Move:", node.move, "\n")
