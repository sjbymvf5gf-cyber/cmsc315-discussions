# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
For this unit, the most important skill or concept learned was about BST. I learned how BST stores data in a way 
that smaller values are sent to the left and larger ones to the right. 
2. What challenges did you encounter, and how did you overcome them?
The biggest challenge encountered this unit was writing recursive methods for inserting, searching and
traversing a tree. While running the code I forgot to return the result in my inorder() causing it to fail completely.
In order to fix it, I had to look back and add the return result at the end.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
A binary search tree is a tree in which each node has at most two children. When inserting, the smaller value gets
added to the left and the larger to the right. Compared to a list or array, using BST helps eliminate nodes when
searching since it doesn't have to check each element one by one.