class TreeNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(data={}, left={}, right={})'.format(
            self.data, self.left, self.right)


class BinarySearchTree(object):

    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.insert(data)

    def data(self):
        return self.root

    def sorted_data(self):
        result = []
        node = self.root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right
        return result

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            node = self.root
            while True:
                next = node.left if data < node.data else node.right
                if not next:
                    break
                node = next
            if data <= node.data:
                node.left = TreeNode(data)
            else:
                node.right = TreeNode(data)
