"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Creating an inventory with 5 value pairs
    inventory = {"P100": 15, "P200": 9, "P300": 25, "P400": 12, "P500": 30}


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    #Printing the current inventory
    print("Initial inventory:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.\n")

    #Search for quantities on 2 existing keys
    print("Quantity for P100:", inventory["P100"])
    print("Quantity for P500:", inventory["P500"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.\n")
    #List before updating values
    print("List before the update:")
    print(inventory)
    #Values to update
    inventory["P100"] = 35
    #List after the update
    print("\nList after the update on P100:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    #List before deletion
    print("\nList before deleting:")
    print(inventory)
    #Value to delete
    del inventory["P100"]
    #List after deletion
    print("\nList after deleting P100:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")
    #Edge case #1: Searching for missing key
    print("Edge Case #1: Searching for missing key")
    missing_key = "P999"
    print("Searching for missing key P999")
    if missing_key in inventory:
        print("Quantity for P999:", inventory[missing_key])
    else:
        print("P999 not found in inventory.\n")

    #Edge Case #2: Using empty dictionary
    print("Edge Case #2: Using empty dictionary")
    empty_inventory = {}
    print("Current inventory:", empty_inventory)

    print("Search in inventory:")
    print(empty_inventory.get("P100", "P100 was not found."))




if __name__ == "__main__":
    main()