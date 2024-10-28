class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def dfs(self, node):
        if node:
            print(node.value, end=' ')  # Pre-order traversal
            self.dfs(node.left)
            self.dfs(node.right)

    def bfs(self):
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)

    print("DFS traversal (Pre-order):")
    tree.dfs(tree.root)

    print("\nBFS traversal:")
    tree.bfs()
