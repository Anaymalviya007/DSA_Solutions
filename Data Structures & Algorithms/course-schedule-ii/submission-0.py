class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            elif state == VISITING: return False
            
            states[node] = VISITING

            for neighbour in g[node]:
                if not dfs(neighbour):
                    return False
            states[node] = VISITED
            order.append(node)
            return True            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order