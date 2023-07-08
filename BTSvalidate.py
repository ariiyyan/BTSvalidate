# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float("-inf"), float("inf"))
        

def validateBstHelper(tree, minValue, maxValue):

    if tree is None:
        return True

    elif  tree.value < minValue or tree.value >= maxValue:
        return False

    leftTree = validateBstHelper(tree.left, minValue , tree.value)
    rightTree = validateBstHelper(tree.right, tree.value, maxValue)

    return leftTree and rightTree
    
