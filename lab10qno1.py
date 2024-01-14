class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return "None,"

    serialized = str(root.value) + ","
    serialized += serialize(root.left)
    serialized += serialize(root.right)
    return serialized

def deserialize(data):
    nodes = data.split(',')
    return deserialize_helper(nodes)

def deserialize_helper(nodes):
    value = nodes.pop(0)
    if value == "None":
        return None
    node = TreeNode(int(value))
    node.left = deserialize_helper(nodes)
    node.right = deserialize_helper(nodes)
    return node

# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Serialize the binary tree
serialized_tree = serialize(root)
print("Serialized Tree:", serialized_tree)

# Deserialize the binary tree
deserialized_root = deserialize(serialized_tree)
