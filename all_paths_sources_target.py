class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result_list = []
        
        _ = self.dfs(graph, result_list, 0, [0])
        
        return result_list
    
    def dfs(self, graph, result_list, pos, path):
        if not graph[pos]:
            result_list.append(path)
            return
        
        for v in graph[pos]:
            _ = self.dfs(graph, result_list, v, path + [v])