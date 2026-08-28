"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for index, current_value in enumerate(lst):
        if current_value == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    #Original List
    numbers = [5, 6, 7, 8, 9]
    print("Original list:", numbers)
    #Inserting number in the beginning
    insert_at(numbers, 0, 4)
    print("After inserting number at the beginning:", numbers)
    #Inserting number in the middle
    insert_at(numbers, 3, 3)
    print("After inserting number in middle:", numbers)
    #Inserting number in the end
    insert_at(numbers, 8, 4)
    print("After inserting number in the end:", numbers)



    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    #Original list
    delete_list = [20, 30, 40, 50, 60]
    print("Original list:", delete_list)
    #Deleting from the list
    front_number = delete_at(delete_list, 0)
    print("Removed number:", front_number)
    print("Updated list:", delete_list)
    #Delete from the middle
    middle_number = delete_at(delete_list, 2)
    print("Removed number:", middle_number)
    print("Updated list:", delete_list)
    #Delete from the end
    last_number = delete_at(delete_list, 2)
    print("Removed number:", last_number)
    print("Updated list:", delete_list)


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    #Original search list
    search_list = [5, 6, 7, 8, 9]
    print("Search list:", search_list)
    #Search specific number
    existing_number = 7
    found_index = search_value(search_list, existing_number)
    print(f"{existing_number} found at index {found_index}")
    #Search number not on list
    missing_number = 15
    found_index = search_value(search_list, missing_number)
    print(f"Searching for {missing_number} results in {found_index}.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    #Printing empty list
    empty_list = []
    print("List before insertion:", empty_list)
    #Inserting to empty list
    insert_at(empty_list, 0, 4)
    print("After insertion:", empty_list)
    #Deleting with invalid index
    invalid_list = delete_at(search_list, 12)
    print("Deleting invalid index 12:", invalid_list)
    #Deleting from empty list
    empty_values = []
    delete_result = delete_at(empty_values, 0)
    print("Deleting from empty list:", empty_values)



if __name__ == "__main__":
    main()