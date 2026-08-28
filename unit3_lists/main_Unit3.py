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
    #Insert the new Keyblade at the specified index.
    lst.insert(index, value)

    #Items at and after insertion point shift one position to the right.
    #Inserting near the beginning will take longer because more items must shift.
    #Inserting near the end means less shifting.



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
    #This will check if the index exists before removing a keyblade.
    # This prevents an IndexError from occurring.
    if(index >= 0 and index < len(lst)):
        return lst.pop(index)

    #Will return None if index is invalid
    return None



def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    index = 0
    #Starting at index 0 will check each item in order.
    #This is a linear search because each item is checked sequentially.
    while index < len(lst):
        #Compare the current keyblade with the value being searched for.
        if lst[index] == value:
            return index

        index +=1

    #will return -1 after the entire list is searched and no keyblade was found.
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

    #Creates Sora's inventory.
    keyblades = ["Kingdom Key", "Three Wishes", "Olympia"]

    print("Keyblades in Sora's Inventory: ", keyblades)

    #Metal Chocobo is placed at the start of his inventory.
    insert_at(keyblades,0,"Metal Chocobo")
    print("Sora obtained Metal Chocobo:",keyblades)

    #Oathkeeper is added in the middle of his inventory.
    insert_at(keyblades,2,"Oathkeeper")
    print("Sora obtained Oathkeeper: ",keyblades)

    #Ultima Weapon is added to the end of his inventory.
    #This inserts Ultima Weapon at the end of inventory.
    insert_at(keyblades,len(keyblades),"Ultima Weapon")
    print("Sora obtained Ultima Weapon: ",keyblades)


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

    #Delete from the beginning
    #Riku takes the first keyblade in Sora's inventory.
    removed = delete_at(keyblades,0)
    print("Riku took Sora's Keyblade:", removed)
    print("Sora's updated inventory: ", keyblades)

    #Keyblade is removed from the middle of Sora's inventory.
    removed = delete_at(keyblades,2)
    print("Keyblade taken:", removed)
    print("Sora's updated inventory: ", keyblades)

    #Removes last keyblade in his inventory.
    #len(keyblades) -1 gives the index of the last item in the list.
    removed = delete_at(keyblades,len(keyblades)-1)
    print("Keyblade taken:", removed)
    print("Sora's updated inventory: ", keyblades)

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

    #This searches for an existing keyblade in the inventory so it can be equipped.
    print("Sora searches for Oathkeeper: ", search_value(keyblades,"Oathkeeper"))

    #This searches for keyblade that does not exist in the inventory.
    print("Sora searches for Divine Rose: ", search_value(keyblades,"Divine Rose"))


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

    #Edge case 1:
    #Sora tries to remove a keyblade from an inventory slot that does not exist.
    removed = delete_at(keyblades,100)
    print("Sora tried to remove a Keyblade from an invalid slot:", removed)

    #Edge case 2:
    #Will try to remove a keyblade from an empty inventory
    #Will return None instead of error
    empty_keyblades = []

    removed = delete_at(empty_keyblades,0)
    print("Sora tried to remove a Keyblade from an empty invetory: ", removed)





if __name__ == "__main__":
    main()