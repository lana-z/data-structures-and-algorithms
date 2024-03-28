import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to a BinaryTree level by level.
    Assumes values are provided in an array representing the desired tree level by level.
    """
    if not values:
        return  # Return if the values list is empty

    root = Node(values.pop(0))  # Create the root node from the first value
    tree.root = root  # Set the root of the tree
    q = Queue()  # Initialize a queue to help with level-order insertion
    q.enqueue(root)  # Enqueue the root

    while values and not q.is_empty():
        node = q.dequeue()  # Dequeue the next node

        if values:
            val = values.pop(0)  # Get the next value for the left child
            if val is not None:  # Only add a node if the value is not None
                node.left = Node(val)
                q.enqueue(node.left)

        if values:
            val = values.pop(0)  # Get the next value for the right child
            if val is not None:  # Only add a node if the value is not None
                node.right = Node(val)
                q.enqueue(node.right)
