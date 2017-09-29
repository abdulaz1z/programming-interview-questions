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
            self.root = Node(data)
        else:
            self.__insert_recursive(self.root, data)
        self.size += 1

    def __find_recursive(self, node, data):
        if not node or data == node.data:
            return node
        if data < node.data:
            return self.__find_recursive(node.left, data)
        return self.__find_recursive(node.right, data)

    def __search(self, data):
        """
        Searches the tree for the node that matches the data
        value. Returns the node if found otherwise None.
        """
        return self.__find_recursive(self.root, data)

    def __get_min_value_node(self, node):
        """
        Returns the node that has the minimum value. A.K.A: The left most node.
        """
        if not node or not node.left:
            return node
        return self.__get_min_value_node(node.left)

    def __delete_recursive(self, node, data):
        """
        It handles 3 possible scenarios:
        1. Node is a leaf. It means it has no left and right child.
        2. Node is parent of a single node (left or right).
        3. Node is parent of two children.

        http://www.algolist.net/Data_structures/Binary_search_tree/Removal
        """
        if not node:
            return node

        if data < node.data:
            node.left = self.__delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self.__delete_recursive(node.right, data)
        else:
            if not node.left: # has no left child
                new_node = node.right
                node = None
                return new_node
            elif not node.right: # has no right child
                new_node = node.right
                node = None
                return new_node

            # Get inorder successor to the right of the tree.
            new_node = self.__get_min_value_node(node.right)
            node.data = new_node.data
            node.right = self.__delete_recursive(node.right, new_node.data)

        return node

    def delete(self, data):
        self.__delete_recursive(self.root, data)

    # Testing-only methods
    def __traverse_inorder(self, node):
        if node is None:
            return
        else:
            self.__traverse_inorder(node.left)
            print node,
            self.__traverse_inorder(node.right)

    def inorder(self):
        """
        Prints the tree in order.
        """
        self.__traverse_inorder(self.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(-4)
    tree.insert(3)
    tree.insert(12)
    tree.insert(9)
    tree.insert(21)
    tree.insert(19)
    tree.insert(25)
    print "Inorder before delete"
    tree.inorder()
    print
    print "Inorder after delete"
    tree.delete(19)
    tree.inorder()
