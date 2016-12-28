import math
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pass
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print data
        data = data.split(',')
        totalLevels = math.log(len(data)+1,2)
        level = 0
        prevLevel = []
        nodeIndex = 1
        
        while level <= totalLevels:
            if level == 0:
                node = TreeNode(data[0])
                prevLevel.append(node)
            else:
                print [item.val for item in prevLevel]
                numNodes = 2**level
                nextNodes = data[nodeIndex:nodeIndex+numNodes]
                currNode = 0
                for i in range(0, len(prevLevel)):
                    # print prevLevel[i].val
                    print i, currNode
                    prevLevel[i].left = nextNodes[currNode]
                    prevLevel[i].right = nextNodes[currNode + 1]
                    currNode += 1

                prevLevel = [TreeNode(n) for n in nextNodes]

                nodeIndex += numNodes
            level += 1

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
codec.deserialize("1, 2, 3, None, None, 4, 5")