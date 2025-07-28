"""
Linked List Data Structure Implementation

This module implements a Singly Linked List data structure using custom Node class.
A linked list is a linear data structure where elements are stored in nodes,
and each node contains data and a reference to the next node.

Author: Educational Python Project
Date: July 28, 2025
"""


class Node:
    """
    A Node class to represent individual elements in the linked list.
    
    Each node contains data and a reference to the next node in the sequence.
    This implements the basic building block of a linked list.
    
    Attributes:
        data: The value stored in the node (can be any data type)
        next: Reference to the next node in the list (None if last node)
    """
    
    def __init__(self, data):
        """
        Initialize a new node with given data.
        
        Args:
            data: The value to be stored in the node
        """
        # Store the data value in the node
        self.data = data
        # Initialize next reference as None (will be set when node is linked)
        self.next = None
    
    def __str__(self):
        """
        String representation of the node for easy display.
        
        Returns:
            str: String representation of the node's data
        """
        return str(self.data)


class LinkedList:
    """
    A Singly Linked List implementation using Node objects.
    
    The LinkedList class provides standard linked list operations:
    - insert: Add elements at various positions
    - delete: Remove elements by value or position
    - search: Find elements in the list
    - display: Show the current list contents
    - size: Get the number of elements
    
    Attributes:
        head (Node): Reference to the first node in the list
        _size (int): Internal counter for the number of elements
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        
        The constructor sets up an empty list with no nodes.
        Using a head pointer to track the beginning of the list.
        """
        # Initialize head pointer as None (empty list)
        self.head = None
        # Keep track of list size for efficiency
        self._size = 0
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        
        This operation has O(1) time complexity as it only updates the head.
        
        Args:
            data: The value to be inserted
        
        Returns:
            None
        """
        # Create a new node with the given data
        new_node = Node(data)
        
        # Point new node to current head (could be None for empty list)
        new_node.next = self.head
        
        # Update head to point to the new node
        self.head = new_node
        
        # Increment the size counter
        self._size += 1
        
        print(f"Inserted '{data}' at the beginning of the list")
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        
        This operation has O(n) time complexity as we need to traverse to the end.
        
        Args:
            data: The value to be inserted
        
        Returns:
            None
        """
        # Create a new node with the given data
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next is not None:
                current = current.next
            
            # Link the last node to the new node
            current.next = new_node
        
        # Increment the size counter
        self._size += 1
        
        print(f"Inserted '{data}' at the end of the list")
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position in the list.
        
        Position 0 means insert at the beginning.
        
        Args:
            data: The value to be inserted
            position (int): The position where to insert (0-indexed)
        
        Returns:
            None
            
        Raises:
            IndexError: If position is negative or greater than list size
        """
        # Validate position
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self._size}")
        
        # If inserting at beginning, use specialized method
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        # Create a new node
        new_node = Node(data)
        
        # Traverse to the position just before insertion point
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        
        # Increment the size counter
        self._size += 1
        
        print(f"Inserted '{data}' at position {position}")
    
    def delete_by_value(self, data):
        """
        Delete the first occurrence of a node with the given value.
        
        This operation has O(n) time complexity in the worst case.
        
        Args:
            data: The value to be deleted
        
        Returns:
            bool: True if deletion was successful, False if value not found
        """
        # Check if list is empty
        if self.head is None:
            print(f"Cannot delete '{data}': List is empty")
            return False
        
        # If head node contains the data to delete
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            print(f"Deleted '{data}' from the list")
            return True
        
        # Search for the node to delete
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                # Remove the node by updating the link
                current.next = current.next.next
                self._size -= 1
                print(f"Deleted '{data}' from the list")
                return True
            current = current.next
        
        # Value not found
        print(f"Value '{data}' not found in the list")
        return False
    
    def delete_at_position(self, position):
        """
        Delete a node at a specific position in the list.
        
        Args:
            position (int): The position of the node to delete (0-indexed)
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If position is invalid or list is empty
        """
        # Check if list is empty
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        
        # Validate position
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self._size}")
        
        # If deleting head node
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            self._size -= 1
            print(f"Deleted '{deleted_data}' from position {position}")
            return deleted_data
        
        # Traverse to the position just before deletion point
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        # Get the data to return and update the link
        deleted_data = current.next.data
        current.next = current.next.next
        self._size -= 1
        
        print(f"Deleted '{deleted_data}' from position {position}")
        return deleted_data
    
    def search(self, data):
        """
        Search for a value in the linked list.
        
        This operation has O(n) time complexity in the worst case.
        
        Args:
            data: The value to search for
        
        Returns:
            int: The position of the first occurrence (0-indexed), or -1 if not found
        """
        # Start from the head and search through the list
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == data:
                print(f"Found '{data}' at position {position}")
                return position
            current = current.next
            position += 1
        
        # Value not found
        print(f"Value '{data}' not found in the list")
        return -1
    
    def display(self):
        """
        Display the current contents of the linked list.
        
        This method provides a visual representation of the list structure.
        Shows the chain of nodes from head to tail.
        
        Returns:
            None
        """
        if self.head is None:
            print("Linked List is empty: []")
            return
        
        # Build a list of values for display
        values = []
        current = self.head
        
        while current is not None:
            values.append(str(current.data))
            current = current.next
        
        # Display the list in a readable format
        print(f"Linked List: {' -> '.join(values)} -> None")
        print(f"Head: {self.head.data}")
    
    def size(self):
        """
        Get the number of elements in the linked list.
        
        This method returns the current size of the list.
        Using internal counter for O(1) time complexity.
        
        Returns:
            int: Number of elements in the list
        """
        print(f"Linked List size: {self._size}")
        return self._size
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if list is empty, False otherwise
        """
        return self.head is None
    
    def clear(self):
        """
        Remove all elements from the linked list.
        
        This method resets the list to its initial empty state.
        
        Returns:
            None
        """
        # Reset head pointer and size counter
        self.head = None
        self._size = 0
        print("Linked List has been cleared")
    
    def get_at_position(self, position):
        """
        Get the data at a specific position without removing it.
        
        Args:
            position (int): The position to access (0-indexed)
        
        Returns:
            The data at the specified position
            
        Raises:
            IndexError: If position is invalid
        """
        # Validate position
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self._size}")
        
        # Traverse to the specified position
        current = self.head
        for i in range(position):
            current = current.next
        
        print(f"Element at position {position}: {current.data}")
        return current.data


# Example usage and testing (only runs when script is executed directly)
if __name__ == "__main__":
    print("=== Linked List Data Structure Demo ===")
    
    # Create a new linked list instance
    linked_list = LinkedList()
    
    # Test empty list
    print("\n1. Testing empty list:")
    linked_list.display()
    print(f"Is empty: {linked_list.is_empty()}")
    
    # Test insertion operations
    print("\n2. Testing insertion operations:")
    linked_list.insert_at_beginning("First")
    linked_list.insert_at_end("Last")
    linked_list.insert_at_position("Middle", 1)
    linked_list.display()
    
    # Test search operations
    print("\n3. Testing search operations:")
    linked_list.search("Middle")
    linked_list.search("NotFound")
    
    # Test access operations
    print("\n4. Testing access operations:")
    linked_list.get_at_position(0)
    linked_list.get_at_position(2)
    
    # Test deletion operations
    print("\n5. Testing deletion operations:")
    linked_list.delete_by_value("Middle")
    linked_list.display()
    
    # Test size operation
    print("\n6. Testing size operation:")
    linked_list.size()
    
    print("\n=== Linked List Demo Complete ===")
