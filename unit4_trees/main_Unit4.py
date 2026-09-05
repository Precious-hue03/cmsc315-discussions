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
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # Stores the grocery item's name in the node.
        self.value = value

        #Grocery item does not have any child nodes when first added.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        #Inventory starts empty.
        self.root = None


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
        #This will start at the root and recursively find where new node belongs.
        self.root = self._insert_recursive(self.root, value)

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
        #if an empty position is found, this creates new node.
        if node is None:
            return Node(value)

        #This will be in alphabetical order
        #Grocery item that come before current one are placed in the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left,value)

        #This will be in alphabetical order
        #Grocery items that come after current one is placed in the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right,value)

        #If the value is the same, it is a duplicate.
        #Duplicate item names are ignored.
        else:
            return node

        return node

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
        #Each Grocery item searched is compared.
        #Determines whether the search should continue left or right.
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        #if there are no nodes, the item was not found.
        if node is None:
            return False

        #Grocery item was found.
        if value == node.value:
            return True

        #Search left subtree if grocery item comes before current one alphabetically.
        if value < node.value:
            return self._search_recursive(node.left,value)

        #otherwise, search right subtree
        return self._search_recursive(node.right,value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root,values)
        return values

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
        #Visiting left, current, then right produces alphabetical order.
        #Smaller values are on the left and larger values on the right.
        if node is not None:
            self._inorder_recursive(node.left,values)

            #add current grocery item.
            values.append(node.value)

            #visit grocery item that come later alphabetically.
            self._inorder_recursive(node.right,values)

    def display_tree(self):
        #displays the tree from the root.
        self._display_tree_recursive(self.root,0)


    def _display_tree_recursive(self,node,level):
        if node is not None:
            #Display right subtree first.
            self._display_tree_recursive(node.right,level + 1)

            #Display the current grocery item.
            print("   " * level + node.value)

            # Display left subtree
            self._display_tree_recursive(node.left, level + 1)



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

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    #Creates grocery item using a BST
    grocery_inventory = BST()

    groceries = ["Milk","Eggs","Rice","Bread", "Chicken",
                 "Grapes","Oranges"]

    #Inserts each grocery item into the tree.
    for grocery in groceries:
        grocery_inventory.insert(grocery)

    print("Grocery items inserted:")
    print(groceries)

    #A BST reduces the search space.
    #Each comparison contiues searching left or right.
    #Does not have to check every grocery item.

    print("\nGrocery Inventory BST:")
    grocery_inventory.display_tree()



    print("\n=== IN-ORDER TRAVERSAL ===")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    sorted_groceries = grocery_inventory.inorder()

    print("Grocery items in alphabetical order:")
    print(sorted_groceries)
    #In-order traversal visits the left subtree, current node, and then right subtree.
    #Smaller values are stored on the left, larger on the right.
    #results are sorted.

    print("\n=== SEARCH TESTS ===")

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

    # Grocery items we want to search for into a list.
    search_tests = [
        "Chicken",
        "Grapes",
        "Cheese",
        "Butter"
    ]

    # Search for each grocery item and display True or False.
    for grocery in search_tests:
        print(f"Searching for {grocery}: "
              f"{grocery_inventory.search(grocery)}")

    #Existing items will return true.
    #Cheese and butter were not added and will return false.

    print("\n=== EDGE CASES ===")

    #Create an empty grocery inventory.
    empty_inventory = BST()

    print("Searching empty inventory:",empty_inventory.search("Milk"))

    print("Empty inventory traversal:", empty_inventory.inorder())

    #Searching an empty tree will return false.
    #There are no nodes to search.
    #Traversing an empty tree returns an empty list.



if __name__ == "__main__":
    main()