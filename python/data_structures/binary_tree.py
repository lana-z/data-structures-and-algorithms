class BinaryTree:
    """
    Provides a basic structure for a binary tree, where each node can have up to two children. It includes methods to insert, search, and traverse the tree in various ways (e.g., in-order, pre-order, post-order).

    Attributes:
    root (Node, optional): The root node of the tree. The tree is initially empty if the root is not specified.

    Methods:
    walk(order): Perform a tree traversal in the specified order ('in-order', 'pre-order', 'post-order') and return a list of values.

    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):
        """
              a
          b      c
        d  e    f  g

        ["a",       "b", "d", "e",      "c", "f", "g"]

        root -> left -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree

        """

        def walk(node):
            """
            task is

            return my result + left node's result + right node's result

            ["a"] + ["b","d","e"] + ["c","f","g"]

            return List

            """

            if node is None:
                return []

            my_result = [node.value]   # ["a"]
            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]

            # ["a"] + ["b","d","e"] + ["c","f","g"]
            return my_result + left_result + right_result


        return walk(self.root)

    def in_order(self):
        """
        left -> root -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """

        def walk(node):
            """
            task is

            return my result + left node's result + right node's result

            ["a"] + ["b","d","e"] + ["c","f","g"]

            return List

            """

            if node is None:
                return []

            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            my_result = [node.value]   # ["a"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]

            # ["b","d","e"] + ["a"] + ["c","f","g"]
            return left_result + my_result + right_result


        return walk(self.root)

    def post_order(self):
        """
        left -> right -> root
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """


        def walk(node):
            if node is None:
                return []

            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]
            my_result = [node.value]   # ["a"]


            return left_result + right_result + my_result


        return walk(self.root)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

