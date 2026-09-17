"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    sorted_list = lst.copy()

    for pass_number in range(len(sorted_list) - 1):
        swapped = False

        for index in range(len(sorted_list) - 1 - pass_number):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1], sorted_list[index]
                )
                swapped = True
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1:
        return lst.copy()

    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return merge(sorted_left_half, sorted_right_half)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    dataset_1 = [42, 17, 89, 3, 56, 24, 71]

    print(f"Dataset 1: {dataset_1}")
    print(f"Bubble Sort: {bubble_sort(dataset_1)}")
    print(f"Merge Sort: {merge_sort(dataset_1)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    dataset_2 = [105, 12, 78, 33, 91, 66, 27]

    print(f"Dataset 2: {dataset_2}")
    print(f"Bubble Sort: {bubble_sort(dataset_2)}")
    print(f"Merge Sort: {merge_sort(dataset_2)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.\n")

    sorted_list = [1, 2, 3, 4, 5, 6, 7]
    print(f"Edge Case #1")
    print(f"Already sorted list: {sorted_list}")
    print(f"Bubble Sort: {bubble_sort(sorted_list)}")
    print(f"Merge Sort: {merge_sort(sorted_list)}")

    duplicate_values = [7, 3, 7, 11, 5, 9]
    print(f"\nEdge Case #2")
    print(f"Duplicate values list: {duplicate_values}")
    print(f"Bubble Sort: {bubble_sort(duplicate_values)}")
    print(f"Merge Sort: {merge_sort(duplicate_values)}")

if __name__ == "__main__":
    main()