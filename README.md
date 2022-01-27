# LinkedListModule
This python module contains 12 important and time efficient functions for dealing with Linked Lists in Python :-
#
1. **listToLink(lst)**
	This function converts the passed list into a linked list and returns the head of the Linked List.
	Time Complexity : O(n)
	Space Complexity : O(1)
      
2. **linkToList(head)**
	This function converts all the nodes from the linked list passed as a head in this function, into list.
	Time Complexity : O(n)
	Space Complexity : O(n)
	
3. **length(head)**
	This funtion returns the length of the linked list.
	Time Complexity : O(n)
	Space Complexity : O(1)
	
4. **append(head, val)**
	This function appends the value passed into the function into the linked list and returns the resulting head. 
	It can used directly without equating it to an another variable to store the head node unless it is an empty linked list.
	Time Complexity : O(n)
	Space Complexity : O(1)

5. **insert(head, val, index)**
	This function inserts the passed value at the provided index into the Linked List and returns the resultant head.
	It can used directly without equating it to an another variable to store the head node unless you are inserting at the 0th index or
	it is an empty linked list.
	Time Complexity : O(n)
	Space Complexity : O(1)
	
6. **pop(head)**
	This function deletes the tail node and return the resulting head node.
	Time Complexity : O(n)
	Space Complexity : O(1)
	
7. **delete(head, index)**
	This function deletes the node at the given index and returns the resulting head node.
	Time Complexity : O(n)
	Space Complexity : O(1)
	
8. **remove(head, val, count=1)**
	This function remove the number of instances (count) of an integer in the Linked List and returns the resulting head node.
	Count is set to a default value of 1 i.e. it would delete only one occurence of the given integer from the Linked List.
	

9. **find(head, val)**
	This function finds the first instance of an element in the Linked List and returns the index.
	If not found it returns -1.
	Time Complexity : O(n)
	Space Complexity : O(1)
	
10. **count(head, val)**
	This function counts and returns the number of instances of the given integer in the Linked List.
	Time Complexity : O(n)
	Space Complexity : O(1)

11. **reverse(head)**
	This function reverses the linked list and returns the new head node i.e. the tail node of the given Linked list.
	Time Complexity : O(n)
	Space Complexity : O(1)	

12. **printll(head)**
	This function prints out the linked list by using the passed head node.
	Time Complexity : O(n)
	Space Complexity : O(1)
