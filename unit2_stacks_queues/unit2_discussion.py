"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

stack = Stack()

print("\nPushing values onto the stack:")
stack.push("First item")
print(" Pushed: First")
stack.push("Second item")
print(" Pushed: Second")
stack.push("Third item")
print(" Pushed: Third")
stack.push("Fourth item")
print(" Pushed: Fourth")

print("\nDemonstrating LIFO (Last-In, First-Out) behavior:")
print(f" Stack is empty? {stack.is_empty()}")
print(f" Top of stack (peek): {stack.peek()}")

print("\nPopping all values from the stack:")
while not stack.is_empty():
    popped = stack.pop()
    print(f" Popped: {popped}")

print("\nTrying to pop from an empty stack:")
result = stack.pop()
print(f" Popped: {result}")

print("\nTrying to peek at an empty stack:")
result = stack.peek()
print(f" Peek: {result}")

print("\nTesting single-item stack:")
stack.push("Only item")
print(f" Pushed one item. Stack is empty? {stack.is_empty()}")
stack.pop()
print(f" Pushed one item. Stack is empty? {stack.is_empty()}")
# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

queue = Queue()

print("\nEnqueueing values to the queue:")
queue.enqueue("First item")
print(" Enqueued: First item")
queue.enqueue("Second item")
print(" Enqueued: Second item")
queue.enqueue("Third item")
print(" Enqueued: Third item")
queue.enqueue("Fourth item")
print(" Enqueued: Fourth item")

print("\nDemonstrating FIFO (First-In, First-Out) behavior:")
print(f" Queue is empty? {queue.is_empty()}")
print(f" Front of queue: {queue.front()}")

print("\nDequeuing values from the queue: ")
while not queue.is_empty():
    dequeued = queue.dequeue()
    print(f" Dequeued: {dequeued}")

print("\nTrying to dequeue from an empty queue:")
result = queue.dequeue()
print(f" Dequeued: {result}")

print("\nTrying to view the front of an empty queue:")
result = queue.front()
print(f" Front: {result}")

print("\nTesting single-item queue:")
queue.enqueue("Only item")
print(f" Enqueued one item. Queue is empty? {queue.is_empty()}")
queue.dequeue()
print(f" Dequeued one item. Queue is empty? {queue.is_empty()}")

# ===============================
# REAL-WORLD SCENARIO
# ===============================

print("\n=== REAL-WORLD SCENARIO ===")
print("\nStack Example: Browser Back Button")
print(" - Each page you visit is pushed onto a stack")
print(" - When you click 'Back', the most recent page is popped")
print(" - This is LIFO: Last page visited is first to be popped\n")

print("Queue Example: Printer Job Queue")
print(" - Each print job is enqueued at the back")
print(" - The printer processes jobs from the front")
print(" - This is FIFO: First job sent is first to print")

if __name__ == "__main__":
    main()
