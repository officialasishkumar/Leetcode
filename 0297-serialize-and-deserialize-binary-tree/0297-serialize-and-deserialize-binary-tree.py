# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s=""
        queue=[]
        queue.append(root)
        while(len(queue)!=0):
            node=queue.pop(0)
            if(node==None):
                s=s+"#,"
            else:
                s=s+str(node.val)+","
            if(node!=None):
                queue.append(node.left)
                queue.append(node.right)
        return s
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        lt=data.split(",")
        if(lt[0]=="#"):
            return None
        lt.pop()
        queue=[]
        root=TreeNode(lt[0])
        queue.append(root)
        i=0
        while(len(queue)!=0):
            node=queue.pop(0)
            i=i+1
            if(lt[i]=="#"):
                node.left=None
            else:
                node.left=TreeNode(int(lt[i]))
                queue.append(node.left)
            i=i+1
            if(lt[i]=="#"):
                node.right=None
            else:
                node.right=TreeNode(int(lt[i]))
                queue.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))