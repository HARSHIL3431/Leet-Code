import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]  # (time, node)
        dist = {}
        
        while heap:
            time, node = heapq.heappop(heap)
            
            if node in dist:
                continue
            
            dist[node] = time
            
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1