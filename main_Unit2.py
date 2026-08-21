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
        #Creates an empty list to store the stack values
        self.stack = []

        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # This will add the newest value to the top of the stack
        self.stack.append(value)
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty? Will return none if empty
        if self.is_empty():
            return None
        #removes and return the recently added value
        return self.stack.pop()
        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek returns the top value without removing it
        if len(self.stack) == 0:
            return None

        return self.stack[len(self.stack) - 1]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        #adds the newest value to the bcak of queue
        self.queue.append(value)
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        #will return none if queue is empty
        if self.is_empty():
            return None
        # If it's not empty, this will remove and return the value from the front
        return self.queue.popleft()
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # will return none if there aren't any values
        if len(self.queue) == 0:
            return None
        # This returns the front value without removing it
        return self.queue[0]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0

        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("\n=== STACK DEMO ===")

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


    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    # This creates a stack of books
    books = Stack()

    # Will add four books to the stack
    books.push("The Red Pyramid")
    books.push("The Hunger Games")
    books.push("The Lightning Thief")
    books.push("Dune")

    #Showing the stack
    print("Books currently in the stack: ", books.stack)

    #This demonstrates LIFO behavior
    print("\nTop book on the stack: ", books.peek())
    print("Removing book from stack: ", books.pop())
    print("Adding new book to stack: ", books.peek())

    #This tests an empty stack
    empty_books = Stack()
    print("\nPop empty stack: ", empty_books.pop())
    print("Peek empty stack: ", empty_books.peek())

    # Test stack with one book
    print("\nVerify a single-item stack becomes empty after removal.")
    one_book = Stack()
    one_book.push("Narnia: The Magician's Nephew")
    print("Removes the only book: ", one_book.pop())
    print("The stack is now empty: ", one_book.is_empty())

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
    returned_books = Queue()

    #adding books to queue
    returned_books.enqueue("The Red Pyramid")
    returned_books.enqueue("The Hunger Games")
    returned_books.enqueue("The Lightning Thief")
    returned_books.enqueue("Dune")

    #Showing the queue
    print("Books currently in the queue: ", list(returned_books.queue))

    #Demonstrates FIFO
    print("First book waiting to be shelved: ", returned_books.front())
    print("Book shelved: ", returned_books.dequeue())
    print("Next book waiting to be shelved: ", returned_books.front())

    #Testing an empty queue
    empty_queue = Queue()
    print("\nTest dequeuing from an empty queue,")
    print("Deque empty queue: ", empty_queue.dequeue())

    print("\nTest viewing the front of an empty queue,")
    print("Front of empty queue: ", empty_queue.front())

    #Test queue with one book
    print("\nVerify a single-item queue becomes empty after removal.")
    one_return = Queue()
    one_return.enqueue("Narnia: The Magician's Nephew")
    print("Shelving the only book: ", one_return.dequeue())
    print("The queue is now empty: ", one_return.is_empty())

if __name__ == "__main__":
    main()
