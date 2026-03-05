n = int(input())
maze = [list(input()) for _ in range(n)]

rows = n
cols = len(maze[0])

start_r = start_c = None
for r in range(rows):
    for c in range(cols):
        if maze[r][c] == "k":
            start_r, start_c = r, c

stack = [(start_r, start_c, 1, set([(start_r, start_c)]))]

longest_path = -1

while stack:
    r, c, dist, visited = stack.pop()


    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
        longest_path = max(longest_path, dist)