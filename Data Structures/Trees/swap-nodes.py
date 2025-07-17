#!/bin/python3

import os
from collections import deque, defaultdict

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
def swapNodes(indexes, queries):
    """Returns a list with the in-order traversal after each swap.

    Parameters
    ----------
    indexes : list[list[int]]
        For node i (1-indexed) `indexes[i-1] = [left, right]`.
    queries : list[int]
        Each `k` indicates that children of nodes whose
        depth is a multiple of `k` should be swapped.

    Returns
    -------
    list[list[int]]
        In-order traversals (list of nodes) for each query.
    """

    n = len(indexes)

    # --- 1) Pre-process depths with BFS ---
    depth = [0] * (n + 1)  # depth[0] unused
    nodes_by_depth = defaultdict(list)

    q = deque([(1, 1)])  # (node, depth)
    while q:
        node, d = q.popleft()
        if node == -1:
            continue
        depth[node] = d
        nodes_by_depth[d].append(node)

        left, right = indexes[node - 1]
        q.append((left, d + 1))
        q.append((right, d + 1))

    # --- 2) Helper function: iterative in-order ---
    def inorder_iterative() -> list[int]:
        result = []
        stack = []
        node = 1  # root
        while stack or node != -1:
            # Go down as much as possible to the left
            while node != -1:
                stack.append(node)
                node = indexes[node - 1][0]  # left child
            # Visit node
            node = stack.pop()
            result.append(node)
            # Go to right subtree
            node = indexes[node - 1][1]
        return result

    final_result = []

    # --- 3) Process each query ---
    for k in queries:
        # 3a) Swap levels that are multiples of k
        d = k
        while nodes_by_depth.get(d):  # only if that level exists
            for node in nodes_by_depth[d]:
                left, right = indexes[node - 1]
                indexes[node - 1][0], indexes[node - 1][1] = right, left
            d += k

        # 3b) Save current in-order
        final_result.append(inorder_iterative())

    return final_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
