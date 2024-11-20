from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        self.root = self.insert_node(self.root, value)

    def insert_node(self, root, value):
        if not root:
            return TreeNode(value)

        if value == root.data:
            return "The node already exists."
        elif value < root.data:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        return root

    def delete(self, value):
        self.root = self.delete_node(self.root, value)

    def delete_node(self, root, value):
        if not root:
            return None
        if value < root.data:
            root.left = self.delete_node(root.left, value)
        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:  # node found
            if not root.left and not root.right:  # no child nodes
                return None
            elif root.left and not root.right:  # left child node
                return root.left
            elif not root.left and root.right:  # right child node
                return root.right
            else:  # full node
                right_min_node = self.find_min_node(root.right)
                root.data = right_min_node.data
                root.right = self.delete_node(root.right, right_min_node.data)
        return root

    def search(self, value):
        return self.find_node(self.root, value)

    def find_node(self, root, value):
        if not root:
            return False

        if value == root.data:
            return True

        if value < self.root.data:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)

    def find_min_node(self, root):
        if not root.left:
            return root
        return self.find_min_node(root.left)

    def find_max_node(self, root):
        if not root.right:
            return root
        return self.find_max_node(root.right)

    def min_node(self):
        return self.find_min_node(self.root).data

    def max_node(self):
        return self.find_max_node(self.root).data

    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, root):
        if not root:
            return 0

        left_tree = self.height_helper(root.left)
        right_tree = self.height_helper(root.right)

        return 1 + max(left_tree, right_tree)

    def depth(self, value):
        return self.depth_helper(self.root, value, 0)

    def depth_helper(self, root, value, current_depth=0):
        if not root:
            return -1

        if value == root.data:
            return current_depth
        elif value < root.data:
            return self.depth_helper(root.left, value, current_depth + 1)
        else:
            return self.depth_helper(root.right, value, current_depth + 1)

    def validate_tree(self):
        return self.validate_tree_helper(self.root, float("-inf"), float("inf"))

    def validate_tree_helper(self, root, lower_bound, upper_bound):
        if not root:
            return True

        if not (lower_bound < root.data < upper_bound):  # validate the node
            return False

        # traverse the left subtree
        left_tree = self.validate_tree_helper(root.left, lower_bound, root.data)

        # traverse the right subtree
        right_tree = self.validate_tree_helper(root.right, root.data, upper_bound)

        # left tree => return a boolean(true or false)
        # right tree => returns a boolean(true or false)
        return left_tree and right_tree

    def lca(self, node1, node2):
        return self.lca_helper(self.root, node1, node2).data

    def lca_helper(self, root, node1, node2):
        if not root:
            return None

        left_tree = self.lca_helper(root.left, node1, node2)
        right_tree = self.lca_helper(root.right, node1, node2)

        if root.data == node1 or root.data == node2:  # return matching nodes
            return root

        if left_tree and right_tree:  # return LCA
            return root

        return left_tree if left_tree else right_tree

    def in_order(self):
        self.in_order_helper(self.root)
        print()

    def in_order_helper(self, root):
        if root:
            self.in_order_helper(root.left)
            print(str(root.data) + "->", end=" ")
            self.in_order_helper(root.right)

    def pre_order(self):
        self.pre_order_helper(self.root)
        print()

    def pre_order_helper(self, root):
        if root:
            print(str(root.data) + "->", end=" ")
            self.pre_order_helper(root.left)
            self.pre_order_helper(root.right)

    def post_order(self):
        self.post_order_helper(self.root)
        print()

    def post_order_helper(self, root):
        if root:
            self.post_order_helper(root.left)
            self.post_order_helper(root.right)
            print(str(root.data) + "->", end=" ")

    def level_order(self):
        node = self.root
        queue = deque([node])
        visited = set()
        while queue:
            current = queue.popleft()
            if current not in visited:
                print(str(current.data) + "->", end=" ")
                visited.add(current)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


if __name__ == "__main__":
    bst = Tree()
    bst1 = Tree()
    nodes = [20, 10, 15, 5, 35, 25, 40, 12, 19]

    for num in nodes:
        bst.insert(num)

    bst.in_order()
    bst.pre_order()
    bst.post_order()
    print(bst.search(35))
    bst.delete(35)
    bst.in_order()
    min_node = bst.min_node()
    max_node = bst.max_node()
    print(min_node, max_node)
    print(bst.height())
    print(bst.level_order())
    print(bst.depth(40))
    print(bst.validate_tree())
    print(bst.lca(10, 19))
