from collections import deque

n = int(input())
board = []

for _ in range(n):
    board.append(input().split())

rows = n
cols = len(board[0])

visited = [[False] * cols for _ in range(rows)]
max_size = 0

for r in range(rows):
    for c in range(cols):
        if board[r][c] == "." and not visited[r][c]:
            queue = deque()
            queue.append((r, c))
            visited[r][c] = True
            size = 1

            while queue:
                cr, cc = queue.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr = cr + dr
                    nc = cc + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == "." and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            size += 1

            if size > max_size:
                max_size = size

print(max_size)