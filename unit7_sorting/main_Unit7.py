"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #Creating a copy so the original prices don't change.
    prices = lst.copy()

    #Goes through the list of store prices.
    for i in range(len(prices) - 1):

        #Compare prices next to each other.
        for j in range(len(prices) - 1 -i):

            #Swap prices if the first price is higher.
            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]

    #returns the store prices from the lowest to highest
    return prices


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #A list with one or no prices is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    #Divide the store prices into tow groups.
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    #Combine the two groups in ascending order.
    prices = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            prices.append(left[i])
            i += 1
        else:
            prices.append(right[j])
            j += 1

    #add any remaining prices.
    prices.extend(left[i:])
    prices.extend(right[j:])

    return prices


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    #Create a new list to store the sorted prices.
    result = []

    #Start at the first price in each list.
    i = 0
    j = 0

    #Compare prices from both lists.
    while i < len(left) and j < len(right):

        #Add the lower price to the result list.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #Combine two sorted groups of prices
    return merge(left,right)


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 Clothing Store ===")
    #Unsorted prices of products at a grocery store.
    clothing_prices = [45, 20, 90, 15, 32, 29, 75]

    #Display the orginal prices and sort them
    #From the lowest to highest using both algorithms.
    print("Original prices:", clothing_prices)
    print("Bubble Sort:", bubble_sort(clothing_prices))
    print("Merge Sort:", merge_sort(clothing_prices))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2: Eletronics Store ===")

    #Unsorted prices of products at an electronics store.
    electronic_prices = [299, 120, 425, 80, 900, 286, 650]

    print("Original prices: ", electronic_prices)
    print("Bubble Sort:", bubble_sort(electronic_prices))
    print("Merge Sort:", merge_sort(electronic_prices))

    #Check whether both algorithms produce the same result.
    print("Results match:",
          bubble_sort(electronic_prices) ==
          merge_sort(electronic_prices))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case #1: Empty list
    # The store has no product prices to sort.
    empty_prices = []

    print("\nEmpty List:")
    print("Original prices:", empty_prices)
    print("Bubble Sort:", bubble_sort(empty_prices))
    print("Merge Sort:", merge_sort(empty_prices))

    # Edge Case #2: Duplicate prices
    # Some products at the store have the same price.
    duplicate_prices = [20, 50, 20, 10, 50, 30, 10]

    print("\nDuplicate Prices:")
    print("Original prices:", duplicate_prices)
    print("Bubble Sort:", bubble_sort(duplicate_prices))
    print("Merge Sort:", merge_sort(duplicate_prices))


if __name__ == "__main__":
    main()