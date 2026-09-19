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


    print("\n=== INSERT OPERATIONS ===")
    #Create an empty dictionary for the music library.
    book_library = {}

    #Add books to the library.
    #The ISBN is the key and the book title is the value.
    book_library["1001"] = "The Lightning Thief"
    book_library["1002"] = "The Sea of Monsters"
    book_library["1003"] = "The Titan's Curse"
    book_library["1004"] = "The Battle of the Labrinth"
    book_library["1005"] = "The Last Olympian"

    #A dictionary behaves like a hash table because it stores information as key value pairs.
    #The ISBN is the key that can be used to quickly find the book title.

    #Display the contents
    print(book_library)


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    #Look up a book using ISBN.
    #The ISBN retrieves the book title associated with it.
    print("Book retrieved:",book_library["1001"])
    print("Book retrieved:",book_library["1002"])

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

    #Display the library before updating the book.
    print("Before update:", book_library)

    #Assigning a new value to an existing ISBN replaces the old book title.
    book_library["1001"] = "Percy Jackson: The Lightning Thief"

    #Display the library after the update.
    print("after update:", book_library)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    #Display the library before removing the book.
    print("Before deletion:", book_library)

    #remove the book form library using its ISBN.
    del book_library["1003"]

    #Display the library after removing the book.
    print("After the deletion:", book_library)

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

    #Edge Case 1:
    #Try to find a book that does not exist in the library.
    #get() returns None instead of causing an error.
    print("Missing book:", book_library.get("1007"))

    #Edge Case 2:
    #Assigning a value to an ISBN that doesn't exist
    #adds a new book instead of updating an existing book.

    book_library["1006"] = "The Chalice of the Gods"

    print("Library after adding new ISBN:", book_library)



if __name__ == "__main__":
    main()