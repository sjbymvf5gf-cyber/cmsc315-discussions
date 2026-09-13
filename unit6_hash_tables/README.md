# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
For this unit, I learned how Python dictionaries work as hash tables and how information is stored as key-value pairs.
Learned how to start off with an empty dictionary and adding key-value pairs. For this example, I sued the SKU as in the
assignment. I was able to insert, lookup, update and delete keys from the inventory.
2. What challenges did you encounter, and how did you overcome them?
One challenge encountered was learning the difference between adding and updating a key. In the beginning, I thought
that assigning a new value to a key would create a duplicate entry. Using keys, it assigns the new value to that key
without creating a copy of it.
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
I learned that hash tables stores data as key-value pairs. This way makes it easier to identify an item within the
inventory. A collision is when two different keys have the same hash location. Using the SKU examples, P100 and P500 have
the same storage position. The way hash tables improve efficiency is by locating a value directly by using its key.
This way if needed, you can insert, lookup, update and delete without the need of checking each item one by one.