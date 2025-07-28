"""
Stack Data Structure Implementation

This module implements a Stack data structure using Python's built-in list.
A stack follows the LIFO (Last In, First Out) principle.

Author: Educational Python Project
Date: July 28, 2025
"""


class Stack:
    """
    A Stack implementation using Python list as the underlying data structure.
    
    The Stack class provides standard stack operations:
    - push: Add an element to the top
    - pop: Remove and return the top element
    - peek: View the top element without removing it
    - is_empty: Check if stack is empty
    - size: Get the number of elements
    
    Attributes:
        _items (list): Internal list to store stack elements
    """
    
    def __init__(self):
        """
        Initialize an empty stack.
        
        The constructor creates an empty list to store stack elements.
        Using a private attribute (_items) to encapsulate the internal structure.
        """
        # Initialize empty list to store stack elements
        self._items = []
    
    def push(self, item):
        """
        Add an element to the top of the stack.
        
        This operation has O(1) time complexity as we append to the end of the list.
        
        Args:
            item: The element to be added to the stack (can be any data type)
        
        Returns:
            None
        """
        # Append the item to the end of the list (top of stack)
        self._items.append(item)
        print(f"Pushed '{item}' onto the stack")
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        This operation has O(1) time complexity as we remove from the end of the list.
        
        Returns:
            The top element from the stack
            
        Raises:
            IndexError: If the stack is empty (underflow condition)
        """
        # Check if stack is empty before popping
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack (Stack Underflow)")
        
        # Remove and return the last element (top of stack)
        popped_item = self._items.pop()
        print(f"Popped '{popped_item}' from the stack")
        return popped_item
    
    def peek(self):
        """
        Return the top element without removing it from the stack.
        
        This operation allows inspection of the top element without modification.
        
        Returns:
            The top element from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        # Check if stack is empty before peeking
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        
        # Return the last element without removing it
        top_item = self._items[-1]
        print(f"Top element is '{top_item}'")
        return top_item
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        This method provides a clean way to test for empty stack condition.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        # Return True if list length is 0, False otherwise
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of elements in the stack.
        
        This method returns the current size of the stack.
        
        Returns:
            int: Number of elements in the stack
        """
        # Return the length of the internal list
        stack_size = len(self._items)
        print(f"Stack size: {stack_size}")
        return stack_size
    
    def display(self):
        """
        Display the current contents of the stack.
        
        This method provides a visual representation of the stack state.
        Shows elements from bottom to top for better understanding.
        
        Returns:
            None
        """
        if self.is_empty():
            print("Stack is empty: []")
        else:
            # Display stack with top element indicated
            print(f"Stack contents (bottom to top): {self._items}")
            print(f"Top -> {self._items[-1]}")
    
    def clear(self):
        """
        Remove all elements from the stack.
        
        This method resets the stack to its initial empty state.
        
        Returns:
            None
        """
        # Clear all elements from the internal list
        self._items.clear()
        print("Stack has been cleared")


# Example usage and testing (only runs when script is executed directly)
if __name__ == "__main__":
    print("=== Stack Data Structure Demo ===")
    
    # Create a new stack instance
    stack = Stack()
    
    # Test empty stack
    print("\n1. Testing empty stack:")
    stack.display()
    print(f"Is empty: {stack.is_empty()}")
    
    # Test push operations
    print("\n2. Testing push operations:")
    stack.push("First")
    stack.push("Second") 
    stack.push("Third")
    stack.display()
    
    # Test peek operation
    print("\n3. Testing peek operation:")
    stack.peek()
    stack.display()  # Stack should remain unchanged
    
    # Test pop operations
    print("\n4. Testing pop operations:")
    stack.pop()
    stack.display()
    
    # Test size operation
    print("\n5. Testing size operation:")
    stack.size()
    
    print("\n=== Stack Demo Complete ===")
