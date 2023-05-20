# LinkedListModule

LinkedListModule is a Python module that provides efficient functions for working with Linked Lists.

## Functions

1. `listToLink(lst)`
   - Converts a given list into a linked list and returns the head of the linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

2. `linkToList(head)`
   - Converts a linked list into a list.
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   
3. `length(head)`
   - Returns the length of the linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
4. `append(head, val)`
   - Appends a value to the end of the linked list and returns the resulting head.
   - This function can be used directly without assigning the returned head to another variable, except for an empty linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

5. `insert(head, val, index)`
   - Inserts a value at the specified index in the linked list and returns the resulting head.
   - This function can be used directly without assigning the returned head to another variable, except when inserting at the 0th index or dealing with an empty linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
6. `pop(head)`
   - Deletes the tail node and returns the resulting head node.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
7. `delete(head, index)`
   - Deletes the node at the specified index in the linked list and returns the resulting head node.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
8. `remove(head, val, count=1)`
   - Removes the specified number of instances (count) of an integer from the linked list and returns the resulting head node.
   - The default value of count is set to 1, which deletes only one occurrence of the given integer from the linked list.
   
9. `find(head, val)`
   - Finds the first instance of an element in the linked list and returns its index.
   - If the element is not found, it returns -1.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
10. `count(head, val)`
    - Counts and returns the number of instances of a given integer in the linked list.
    - Time Complexity: O(n)
    - Space Complexity: O(1)

11. `reverse(head)`
    - Reverses the linked list and returns the new head node (i.e., the previous tail node).
    - Time Complexity: O(n)
    - Space Complexity: O(1)

12. `printll(head)`
    - Prints the linked list using the given head node.
    - Time Complexity: O(n)
    - Space Complexity: O(1)

## Usage

Feel free to use this module to efficiently perform operations on Linked Lists in your Python projects. To use the module, simply import it into your Python script or interactive session:

```python
import LinkedListModule
