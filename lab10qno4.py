class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def updateHeight(self, node):
        if node is not None:
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.updateHeight(y)
        self.updateHeight(x)

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.updateHeight(x)
        self.updateHeight(y)

        return y

    def in
