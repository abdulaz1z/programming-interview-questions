class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __insert_recursive(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insert_recursive(node.left, data)
        else: 
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insert_recursive(node.right, data)

    def insert(self, data):
        if self.root is None:
            print "root:", data
            self.root = Node(data)
        else:
            self.__insert_recursive(self.root, data)
        self.size += 1

    def __delete_recursive(self, node, data):
        if node.left is None and node.right is None:
            node = None
        elif node.right is None:
            old_left = node.left

    def delete(self, data):
        pass

    # Testing only methods
    def __traverse_inorder(self, node):
        if node is None:
            return
        else:
            self.__traverse_inorder(node.left)
            print node
            self.__traverse_inorder(node.right)

    def inorder(self):
        """
        Prints the tree in order.
        """
        self.__traverse_inorder(self.root)


if __name__=="__main__":
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(10)
    tree.insert(3)
    tree.insert(1)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(14)
    tree.insert(13)
    tree.inorder()
