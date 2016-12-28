# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
            
        nodeDict = {}
        queue = [node]
        copyNode = UndirectedGraphNode(node.label)
        nodeDict[node] = copyNode
        
        while len(queue) > 0:
            currNode = queue.pop(0)
            
            for neighbor in currNode.neighbors:
                if neighbor in nodeDict:
                    nodeDict[currNode].neighbors.append(nodeDict[neighbor])
                else:
                    copy = UndirectedGraphNode(neighbor.label)
                    nodeDict[neighbor] = copy
                    nodeDict[currNode].neighbors.append(copy)
                    queue.append(neighbor)
        
        return nodeDict[node]
                