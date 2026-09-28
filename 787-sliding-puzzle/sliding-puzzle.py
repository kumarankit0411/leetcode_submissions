class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ""

        for row in board:
            for num in row:
                start += str(num)

        visited = set()

        queue = deque()

        target = "123450"

        queue.append((start, 0))

        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        while queue:
            config, moves = queue.popleft()

            if config in visited:
                continue
            
            visited.add(config)

            if config == target:
                return moves

            zeroIdx = config.index("0")

            for nextIdx in directions[zeroIdx]:
                new_config = list(config)

                new_config[zeroIdx], new_config[nextIdx] = \
                    new_config[nextIdx], new_config[zeroIdx]

                new_config = "".join(new_config)
                if new_config not in visited:
                    queue.append((new_config, moves + 1))

        return -1