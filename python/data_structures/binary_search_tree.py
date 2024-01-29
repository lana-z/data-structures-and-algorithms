from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
     A Binary Search Tree is a node-based binary tree data structure which has the following properties:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - The left and right subtree each must also be a binary search tree.
    - There must be no duplicate nodes.

    """

    def add(self, value):

        # wrap value in Node
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        def walk(node_to_ask, node_to_add):
            """
            Look for the right spot to "sit" aka be added
            inspect each node and either
            a: "sit" next to it in correct spot
            b: move on in the correct direction
            """

            if node_to_add.value < node_to_ask.value:
                # go left
                if node_to_ask.left is None:
                    node_to_ask.left = node_to_add
                    return
                else:
                    walk(node_to_ask.left, node_to_add)

            elif node_to_add.value > node_to_ask.value:
                if node_to_ask.right is None:
                    node_to_ask.right = node_to_add
                    return
                else:
                    walk(node_to_ask.right, node_to_add)

        walk(self.root, new_node)



    def contains(self, value):

        def walk(node_to_ask):
            if node_to_ask is None:
                return False
            if value == node_to_ask.value:
                return True
            elif value < node_to_ask.value:
                return walk(node_to_ask.left)
            else:  # if value_to_find > node_to_ask.value
                return walk(node_to_ask.right)

        return walk(self.root)
