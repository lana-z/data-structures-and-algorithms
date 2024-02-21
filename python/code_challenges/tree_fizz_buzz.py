
# def fizz_buzz(value):
#     if value % 3 == 0 and value % 5 == 0:
#         return "FizzBuzz"
#     elif value % 3 == 0:
#         return "Fizz"
#     elif value % 5 == 0:
#         return "Buzz"
#     else:
#         return str(value)

# def fizz_buzz_tree(tree):
#     cloned_tree = tree.clone()

#     def walk(node):
#         if node is None:
#             return

#         node.value = fizz_buzz(node.value)

#         for child in node.children:
#             walk(child)

#     walk(cloned_tree.root)

#     return cloned_tree
