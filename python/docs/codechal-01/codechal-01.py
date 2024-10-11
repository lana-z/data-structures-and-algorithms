def reverse_list(items):
    left_index = 0
    right_index = len(items) - 1
    while left_index < right_index:
        items[left_index], items[right_index] = items[right_index], items[left_index]
        left_index += 1
        right_index -= 1

    return items


# Big O Time O(1), Space O(1)

