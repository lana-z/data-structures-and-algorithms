from data_structures.binary_tree import BinaryTree, Node
from data_structures.hashtable import Hashtable

def tree_intersection(tree_a, tree_b):
    hashtable = Hashtable()
    result_set = set()

    def traverse_and_store(node):
        if node:
            hashtable.set(node.value, True)
            traverse_and_store(node.left)
            traverse_and_store(node.right)

    def traverse_and_check(node):
        if node:
            if hashtable.has(node.value):
                result_set.add(node.value)
            traverse_and_check(node.left)
            traverse_and_check(node.right)

    # Traverse the first tree and store values
    traverse_and_store(tree_a.root)

    # Traverse the second tree and check for common values
    traverse_and_check(tree_b.root)

    return list(result_set)
