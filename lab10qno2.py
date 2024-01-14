class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    def height_and_diameter(node):
        if not node:
            return 0, 0  # Height, Diameter

        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)

        current_height = 1 + max(left_height, right_height)
        current_diameter = max(left_height + right_height, left_diameter, right_diameter)

        return current_height, current_diameter

    _, diameter = height_and_diameter(root)
    return diameter

# Example usage:
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)

print("Diameter of the binary tree:", diameter_of_binary_tree(root))
