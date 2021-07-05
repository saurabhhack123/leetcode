class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        graph = collections.defaultdict(list)
        chars = set("".join(words))
        indegree = { ch: 0 for ch in chars }
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            for x,y in zip(word1, word2):
                if x!=y:
                    graph[x].append(y)
                    indegree[y]+=1
                    break
            else:
                if len(word1)>len(word2):
                    return ""
        
        print(graph)    
        queue = []
        
        for ch,val in indegree.items():
            if val==0:
                queue.append(ch)
            
        result = ''
        print(queue)
        
        while queue:
            node = queue.pop(0)
            
            result += node
            
            for neighbors in graph[node]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    queue.append(neighbors)
        
        print(graph)
                
        return result * (set(result) == chars)

                
        
        
        
            
            
        

        
        
