"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None
        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

        pass

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)
        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #This starts the node if nothing is found.
        if node is None:
            return Node(value)
        #Insert value into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        #Insert value into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        #Any values that are similar will be ignored.
        return node
        pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        #If node is null, the value is not found.
        if node is None:
            return False
        #If node found, it will be True.
        if node.value == value:
            return True
        #Searching for left smaller values.
        if value < node.value:
            return self._search_recursive(node.left, value)
        #Searching for right larger values.
        return self._search_recursive(node.right, value)
        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        result = []

        self._inorder_recursive(self.root, result)
        return result
        pass

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)
        pass


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")
    #Creating a BST list
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]

    for val in values:
        bst.insert(val)

    print(f"Values inserted into the BST: {values}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    sorted_values = bst.inorder()

    print(f"Values sorted into the BST: {sorted_values}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    #Searching for values existing in the BST. Used bst.search(existing_value1) to create a search function.
    existing_value1 = 30
    existing_value2 = 70
    existing_value1_search = bst.search(existing_value1)
    existing_value2_search = bst.search(existing_value2)
    print(f"Search for: {existing_value1} returns {existing_value1_search}")
    print(f"Search for: {existing_value2} returns {existing_value2_search}")
    #Searching for values not in BST. Used bst.search(nonexistent_value1) to create a search function.
    missing_value1 = 10
    missing_value2 = 100
    nonexistent_value1_search = bst.search(missing_value1)
    nonexistent_value2_search = bst.search(missing_value2)
    print(f"Search for: {missing_value1} returns {nonexistent_value1_search}")
    print(f"Search for: {missing_value2} returns {nonexistent_value2_search}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    empty_bst = BST()
    print(f"Traverse empty BST: {empty_bst.inorder()} (Expected: [])")
    print(f"Search empty BST: {empty_bst.search(0)} (Expected: False)")
    #Inserting duplicate values into the BST. Any duplicate should be skipped.
    duplicate_bst = BST()
    duplicate_bst.insert(95)
    duplicate_bst.insert(96)
    duplicate_bst.insert(96)
    duplicate_bst.insert(95)
    duplicate_bst.insert(97)
    print(f"Duplicate values BST: {duplicate_bst.inorder()} (Expected: [95, 96, 97])")

    single_node_bst = BST()
    single_node_bst.insert(42)
    print(f"Single node BST: {single_node_bst.inorder()} (Expected: [42])")
    print(f"Search single node BST: {single_node_bst.search(42)} (Expected: True)")

if __name__ == "__main__":
    main()