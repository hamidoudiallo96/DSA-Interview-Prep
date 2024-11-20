from binary_search_tree import TreeNode

class Codec:
    def build_tree(self):
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.right = TreeNode(70)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(40)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(80)
        return root


    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" => ")
            self.in_order(root.right)

    def serialize(self, root):
        res = []

        def dfs(root):
            if not root:
                res.append("#")
                return

            res.append(str(root.data))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(res)

    def deserialize(self, res):
        self.i = 0

        def dfs():
            if self.i >= len(res) or res[self.i] == "#":
                self.i += 1
                return None

            root = TreeNode(int(res[self.i]))
            self.i += 1

            root.left, root.right = dfs(), dfs()
            return root

        return dfs()




def main():
    tree = Codec()
    root = tree.build_tree()
    tree.in_order(root)
    serialized_tree = tree.serialize(root)
    print()
    print(serialized_tree)
    print()
    deserialized_tree = tree.deserialize(serialized_tree.split(","))
    tree.in_order(deserialized_tree)
    # node_count = tree.count_actual_nodes(serialized_tree)
    # print()
    # print(node_count)

    def count_actual_nodes(serialized_str):
    # What logic would you use to count only valid nodes?
    # Remember: you have both numbers and "None"/"#" in the string
        serialized_arr = serialized_str.split(",")
        count = 0
        for char in serialized_arr:
            if char not in "#/None":
                count += 1
        return count
    node_count = count_actual_nodes(serialized_tree)
    print(node_count)
if __name__ == "__main__":
    main()
