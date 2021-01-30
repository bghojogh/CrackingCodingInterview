#### Question: Given parent-child relationships, determine the family members which have no parents or one parent.

def main():
    pairs = [(1,2), (2,3), (1,4), (4,3), (5,2), (1,6)]
    print(find_families_BFS(pairs))
    print(find_families_DFS(pairs, node=1)[0])
    
# output:
# [1, 4, 6, 5]
# [1, 5, 4, 6]
    
def find_families_DFS(pairs, node, answer=[], visited=[]):
    if node in visited:
        return answer, visited
    visited.append(node)
    parents = find_parents(pairs, node)
    if len(parents) == 1 or len(parents) == 0:
        answer.append(node)
    neighbors = find_neighbors(pairs, node)
    for neighbor in neighbors:
        answer, visited = find_families_DFS(pairs, neighbor, answer, visited)
    return answer, visited
    
def find_families_BFS(pairs):
    answer = []
    queue = []
    visited = []
    node = pairs[0][0]
    queue.append(node)
    visited.append(node)
    parents = find_parents(pairs, node)
    if len(parents) == 1 or len(parents) == 0:
        answer.append(node)
    while len(queue) != 0:
        node = queue[0]
        queue = queue[1:]
        neighbors = find_neighbors(pairs, node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(node)
                queue.append(neighbor)
                parents = find_parents(pairs, neighbor)
                if len(parents) == 1 or len(parents) == 0:
                    answer.append(neighbor)
    return answer
    
def find_parents(pairs, node):
    parents = []
    for pair in pairs:
        if node == pair[1]:
            parents.append(pair[0])
    return parents

def find_children(pairs, node):
    children = []
    for pair in pairs:
        if node == pair[0]:
            children.append(pair[1])
    return children

def find_neighbors(pairs, node):
    parents = find_parents(pairs, node)
    children = find_children(pairs, node)
    neighbors = parents
    neighbors.extend(children)
    return neighbors

if __name__ == "__main__":
    main()
