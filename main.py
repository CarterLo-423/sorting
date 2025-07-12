def merge_two_sorted_lists(left_list, right_list):
    merged_result = []
    left_index = 0
    right_index = 0

    # Compare elements from both lists and add the smaller one
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_result.append(left_list[left_index])
            left_index += 1
        else:
            merged_result.append(right_list[right_index])
            right_index += 1

    # Add any remaining elements from both lists
    merged_result.extend(left_list[left_index:])
    merged_result.extend(right_list[right_index:])
    return merged_result

def merge_sort(numbers_list):
    # Base case: if list has 1 or no elements, it's already sorted
    if len(numbers_list) <= 1:
        return numbers_list
    # Split the list in half
    middle_index = len(numbers_list) // 2
    left_half = merge_sort(numbers_list[:middle_index])
    right_half = merge_sort(numbers_list[middle_index:])
    
    # Merge the sorted halves
    return merge_two_sorted_lists(left_half, right_half)

def quickSort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list
    
    pivot_element = numbers_list[0]
    smaller_numbers = []
    larger_numbers = []

    for current_number in numbers_list[1:]:
        if current_number <= pivot_element:
            smaller_numbers.append(current_number)
        else:
            larger_numbers.append(current_number)
    return quickSort(smaller_numbers)+[pivot_element]+quickSort(larger_numbers)

    
if __name__ == "__main__":
    # Test the sorting algorithms
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_numbers)
    
    # Test Quick Sort
    quick_sorted = quickSort(test_numbers.copy())
    print("Quick Sort result:", quick_sorted)
    
    # Test Merge Sort
    merge_sorted = merge_sort(test_numbers.copy())
    print("Merge Sort result:", merge_sorted)