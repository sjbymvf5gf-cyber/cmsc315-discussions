"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #Create a loop to check for a value and return it. Returns -1 if not found
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    #Initialize the left and right boundaries
    left = 0
    right = len(lst) - 1
    #Continue the search while search space is valid. Discard either side depending on the value
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    #Create small dataset
    small_dataset = [5, 12, 18, 23, 30, 42, 55, 67]

    #Search for number in dataset
    target_number = 23
    linear_result = linear_search(small_dataset, target_number)
    binary_result = binary_search(small_dataset, target_number)
    print(f"Small list: {small_dataset}\n")
    print(f"Search for: {target_number}")
    print(f"Linear search: {linear_result}")
    print(f"Binary search: {binary_result}\n")

    #Search for number not in dataset
    missing_number = 70
    linear_result_missing = linear_search(small_dataset, missing_number)
    binary_result_missing = binary_search(small_dataset, missing_number)
    print(f"Search for missing number: {missing_number}")
    print(f"Linear search for missing number: {linear_result_missing}")
    print(f"Binary search for missing number: {binary_result_missing}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    #Create a large dataset
    large_dataset = list(range(10000))

    #Search for number within dataset
    large_target_number = 9999
    linear_result_large = linear_search(large_dataset, large_target_number)
    binary_result_large = binary_search(large_dataset, large_target_number)
    print(f"Large list size: {len(large_dataset)}")
    print(f"Search for: {large_target_number}")
    print(f"Linear search: {linear_result_large}")
    print(f"Binary search: {binary_result_large}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #Edge Case 1 - Search in an emtpy list
    print("Edge Case #1 - Search in an empty list")
    empty_list = []
    empty_number = 5
    empty_result_linear = linear_search(empty_list, empty_number)
    empty_result_binary = binary_search(empty_list, empty_number)
    print(f"Empty list: {empty_list}, search for: {empty_number}")
    print(f"Linear search: {empty_result_linear}")
    print(f"Binary search: {empty_result_binary}\n")

    #Edge Case 2 - Dataset with only 1 number
    print("Edge Case #2 - Dataset with only 1 number")
    single_number_list = [33]
    number_check = 33
    single_number_result_linear = linear_search(single_number_list, number_check)
    single_number_result_binary = binary_search(single_number_list, number_check)
    print(f"Single number list: {single_number_list}, search for: {number_check}")
    print(f"Linear search: {single_number_result_linear}")
    print(f"Binary search: {single_number_result_binary}")

if __name__ == "__main__":
    main()