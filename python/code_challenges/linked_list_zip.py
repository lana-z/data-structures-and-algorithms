from data_structures.linked_list import LinkedList


def zip_lists(a, b):

    zip_lists = LinkedList()

    #check for empty lists
    if not a.head:
        return b
    if not b.head:
        return a

    current_a = a.head
    current_b - b.head

    while current_a or current_b:
        # save the next pointers
        if current_a:
            zip_lists.append(current_a.value)
            current_a = current_a.next

        if current_b:
            zip_lists.append(current_b.value)
            current_a.next = current_b.next

    return zip_lists
