from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    if tree.root is None:
        return []

    q=Queue()
    values=[]

    q.enqueue(tree.root)

    while not q.is_empty():
        node=q.dequeue()
        values.append(node.value)

        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)

    return values
