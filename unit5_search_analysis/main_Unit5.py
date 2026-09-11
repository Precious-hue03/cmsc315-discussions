"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #Linear search has O(n) time complexity because it checks every restaurant order in the list.
    for i in range(len(lst)):
        #Check if current order matches the target order.
        if lst[i] == target:
            #Return the index where the order was found.
            return i

    #Return -1 if the order isn't found
    return -1



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    #Start searching the entire list.
    low = 0
    high = len(lst) -1

    while low <= high:
        #Find the middle order in the current search.
        mid = (low + high) // 2

        #Check if the middle order is the target order.
        if lst[mid] == target:
            return mid

        #If the target is larger, eliminate the lower half.
        elif lst[mid] < target:
            low = mid + 1

        #If the target is smaller, eliminate the upper half.
        else:
            high = mid -1

    #The target order was not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    #Small sorted list of restaurant order numbers.
    small_orders = [101, 115, 130, 145, 160, 175]

    #Search for an order that exists.
    existing_order = 145

    print("Restaurant orders:", small_orders)
    print("Searching for order:", existing_order)

    linear_result = linear_search(small_orders, existing_order)
    binary_result = binary_search(small_orders, existing_order)

    print("Linear search index:",linear_result)
    print("Binary search index:",binary_result)
    #Both searches return index 3 because order 145 exists in the list.

    #Search for an order that doesn't exist.
    missing_order = 200

    print("\nSearching for order:", missing_order)

    linear_result = linear_search(small_orders, missing_order)
    binary_result = binary_search(small_orders, missing_order)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    #Both searches return -1 because order 200 is not in the list.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    #Create a larger sorted list of restaurant order numbers.
    larger_orders = list(range(100, 1100))

    target_order = 950

    print("Searching for order:",target_order)

    linear_result = linear_search(larger_orders, target_order)
    binary_result = binary_search(larger_orders, target_order)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    #Linear search may check orders one at a time.
    #Binary search repeatedly removes half of the remaining orders.
    #This makes binary search more efficient as the dataset becomes larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    #Edge case 1: Empty restaurant order list.
    empty_orders = []

    print("Empty list search:")
    print("Linear search:", linear_search(empty_orders, 101))
    print("Binary search:", binary_search(empty_orders,101))
    #Both will return -1 becasue there are no orders to search.


    #Edge case 2: Target is the last order in the list.
    last_order = 175

    print("\nSearching for the last order:", last_order)
    print("linear search:", linear_search(small_orders,last_order))
    print("Binary search:", binary_search(small_orders,last_order))

    #Order 175 is at index 5.
    #Linear search must go through previous orders before finding it.
    #Binary search can reduce the search area instead.


if __name__ == "__main__":
    main()