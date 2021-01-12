from queue import PriorityQueue
import copy


class Maze:
    start = (0, 0)
    key = (0, 0)
    goal = (0, 0)
    column = 0
    row = 0
    keynumber = 0
    keylist = []
    map = []
    maze = []
    def __init__(self, filename):
        self.keylist.clear()
        self.keynumber = 0
        with open(filename, 'r') as f:
            self.map = []
            self.map.clear()
            self.maze = []
            self.maze.clear()
            n, self.column, self.row = [int(x) for x in f.readline().strip().split(' ')]
            for l in f:
                line = [int(x) for x in l.strip()]
                self.map.append(line)
                self.maze.append(line)
                for x in range(0, len(line)):
                    if line[x] == 3:
                        self.start = (len(self.map)-1, x)
                    elif line[x] == 4:
                        self.goal = (len(self.map)-1, x)
                    elif line[x] == 6:
                        self.key = (len(self.map)-1, x)
                        self.keylist.append(self.key)
                        self.keynumber += 1

    def position_check(self, position):
        if position[0] < 0 or position[0] >= self.column or position[1] < 0 or position[1] >= self.row:
            return False
        if self.map[position[0]][position[1]] != 1:
            return True
        else:
            return False

    def move(self, position, direction):
        new = (position[0] + direction[0], position[1] + direction[1])

        if self.position_check(new):
            return new

        return None

    def coordinate(self):
        ret = []
        ret.clear()

        for i in range(0, self.column):
            ret.append([(i, x) for x in range(0, self.row)])

        return ret

    def tracking(self, path, goal):
        node = goal

        while path[node[0]][node[1]] != node:
            if self.map[node[0]][node[1]] == 2 or self.map[node[0]][node[1]] == 6:
                self.map[node[0]][node[1]] = 5

            node = path[node[0]][node[1]]

    def dfs(self, start, limit, path):
        mz = copy.deepcopy(self)
        mz.map = copy.deepcopy(self.map)
        mz.maze = copy.deepcopy(self.maze)
        stack = []
        stack.clear()
        time = 0
        stack.append((start, 0, start))
        while not len(stack) <= 0:
            if limit<=0:
                return (time, False, 0)
            node = stack.pop()
            position, length, previous = node
            path[position[0]][position[1]] = previous
            mz.map[position[0]][position[1]] = 1

            if mz.maze[position[0]][position[1]] == 4:
                self.tracking(path, position)
                return (time, True, length)

            elif mz.maze[position[0]][position[1]] == 6:
                self.keynumber = self.keynumber-1
                self.tracking(path, position)
                self.start = (position[0], position[1])
                return (time, False, length)

            for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
                mv = mz.move(position, direction)
                if mv is not None:
                    stack.append((mv, length + 1, position))
            time = time + 1
            limit = limit - 1
        return (time, False, 0)

    def bfs_helper(self, start, goal, heuristic):
        mz = copy.deepcopy(self)
        mz.map = copy.deepcopy(self.map)
        q = PriorityQueue()
        time = 0
        path = self.coordinate()
        q.put((0, (start, 0, start)))

        while not q.empty():
            node = q.get()
            position, length, previous = node[1]

            path[position[0]][position[1]] = previous
            mz.map[position[0]][position[1]] = 1

            if position == goal:
                self.tracking(path, goal)
                return (time, length)

            for dr in [(1,0),(0,1),(-1,0),(0,-1)]:
                mv = mz.move(position, dr)
                if mv is not None:
                    q.put((heuristic(position, goal, length + 1), (mv, length + 1, position)))

            time = time + 1
        return (0, 0)

    def ids(self):
        limit = 1
        time = 0
        length = 0
        path = self.coordinate()
        while limit < self.column*self.row:
            ret = self.dfs(self.start, limit, path)
            time += ret[0]
            if ret[2] != 0:
                length += ret[2]
            if ret[1] and self.keynumber == 0:
                return (time, length)
            limit = limit + self.row
        return (0,0)

    def gbfs(self):
        heuristic = lambda a, b, c: abs(a[0] - b[0]) + abs(a[1] - b[1])
        self.keylist.sort(key=lambda x: [x[1], x[0]])
        gbfs_time = 0
        gbfs_length = 0

        r = self.bfs_helper(self.start, self.keylist[0], heuristic)
        gbfs_time += r[0]
        gbfs_length += r[1]

        for i in range(0, self.keynumber - 1):
            r = self.bfs_helper(self.keylist[i], self.keylist[i + 1], heuristic)
            gbfs_time += r[0]
            gbfs_length += r[1]

        r = self.bfs_helper(self.keylist[self.keynumber - 1], self.goal, heuristic)
        gbfs_time += r[0]
        gbfs_length += r[1]
        return (gbfs_time, gbfs_length)

    def a_star(self):
        heuristic = lambda a, b, c: abs(a[0] - b[0]) + abs(a[1] - b[1]) + c
        self.keylist.sort(key=lambda x: [x[1], x[0]])
        astartime = 0
        astartlength = 0

        r = self.bfs_helper(self.start, self.keylist[0], heuristic)
        astartime += r[0]
        astartlength += r[1]

        for i in range(0, self.keynumber - 1):
            r = self.bfs_helper(self.keylist[i], self.keylist[i + 1], heuristic)
            astartime += r[0]
            astartlength += r[1]

        r = self.bfs_helper(self.keylist[self.keynumber - 1], self.goal, heuristic)
        astartime += r[0]
        astartlength += r[1]
        return (astartime, astartlength)

    def bfs_b(self, start):
        mz = copy.deepcopy(self)
        mz.map = copy.deepcopy(self.map)
        mz.maze = copy.deepcopy(self.maze)
        q = PriorityQueue()
        time = 0
        path = self.coordinate()
        q.put((0,(start, 0, start)))
        while not q.empty():
            node = q.get()
            position, length, previous = node[1]
            path[position[0]][position[1]] = previous
            mz.map[position[0]][position[1]] = 1
            if mz.maze[position[0]][position[1]] == 4:
                self.tracking(path, position)
                return (time, length, True)
            elif mz.maze[position[0]][position[1]] == 6:
                self.keynumber = self.keynumber -1
                self.tracking(path, position)
                self.start = (position[0], position[1])
                return (time, length, False)
            for dr in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                mv = mz.move(position, dr)
                if mv is not None:
                    q.put((0,(mv, length + 1, position)))

            time = time + 1
        return (0, 0, False)


    def bfs(self):
        bfstime = 0
        bfslength = 0
        while True:
            ret = self.bfs_b(self.start)
            bfstime += ret[0]
            bfslength += ret[1]
            if ret[2] and self.keynumber == 0:
                return (bfstime, bfslength)


def astar_run(maze: str):
    mz = Maze(maze+".txt")
    time, length = mz.a_star()
    with open(maze + '_A_star_output.txt', 'w') as f:
        for line in mz.map:
            for x in line:
                f.write(str(x))
            f.write('\n')
        f.write('---\n')
        f.write('length=' + str(length) + '\n')
        f.write('time=' + str(time) + '\n')


def bfs_run(maze: str):
    mz = Maze(maze+".txt")
    time, length = mz.bfs()
    with open(maze + '_BFS_output.txt', 'w') as f:
        for line in mz.map:
            for x in line:
                f.write(str(x))
            f.write('\n')
        f.write('---\n')
        f.write('length=' + str(length) + '\n')
        f.write('time=' + str(time) + '\n')


def gbfs_run(maze: str):
    mz = Maze(maze+".txt")
    time, length = mz.gbfs()
    with open(maze + '_GBFS_output.txt', 'w') as f:
        for line in mz.map:
            for x in line:
                f.write(str(x))
            f.write('\n')
        f.write('---\n')
        f.write('length=' + str(length) + '\n')
        f.write('time=' + str(time) + '\n')


def ids_run(maze: str):
    mz = Maze(maze+".txt")
    time, length = mz.ids()
    with open(maze + '_IDS_output.txt', 'w') as f:
        for line in mz.map:
            for w in line:
                f.write(str(w))
            f.write('\n')
        f.write('---\n')
        f.write('length=' + str(length) + '\n')
        f.write('time=' + str(time) + '\n')


def functioncall(maze : str):
    astar_run(maze)
    gbfs_run(maze)
    bfs_run(maze)
    ids_run(maze)


if __name__ == '__main__':
    functioncall('Maze_1')
    functioncall('Maze_2')
    functioncall('Maze_3')
    functioncall('Maze_4')
