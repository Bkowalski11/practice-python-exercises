def binary_search(ordered_list, target):
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        mid = (low + high) //2
        guessed_number = ordered_list[mid]
        if guessed_number == target:
            return True
        elif guessed_number > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

numb = [1, 3, 5, 30, 42, 43, 500]
print(binary_search(numb, 42))