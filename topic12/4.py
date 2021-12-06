""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


# def checkBST(root, prev = None, left=False, right=False):
#     # print(root)
#     # print(root.__dict__)
#     res1 = True
#     res2 = True
#     if root.left is not None:
#         res1 = checkBST(root.left, root, True)
#     if left:
#         return True if root.data < prev.data and res1 else False

#     if root.right is not None:
#         res2 = checkBST(root.right, root, False, True)
#     if right:
#         return True if root.data > prev.data else False

#     return True if res1 and res2 else False
        
        
data = []

def checkBST(root, prev = None):
    if root is not None:
        checkBST(root.left, root)
        data.append(root.data)
        checkBST(root.right, root)
    if prev is None:
        return True if all([True if data[x] < data[x+1] else False for x in range(len(data)-1)]) else False
        
        