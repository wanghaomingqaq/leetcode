#    5
#   / \
#  2   6
# / \
#1   3
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrder(tree, array=[]):
    if tree == None:
        return []
    else:
        #这个试中序遍历，把根节点root放在中间，中间是append,
        #如果是前序遍历那么就是先append（tree.value)在左右
        inOrder(tree.left,array)
        array.append(tree.value)
        inOrder(tree.right,array)
    return array

root = BST(5)
root.left = BST(2)
root.right = BST(6)
root.left.left = BST(1)
root.left.right = BST(3)
print(inOrder(root))