"""
Queue Data Structure Implementation

This module implements a Queue data structure using Python's built-in list.
A queue follows the FIFO (First In, First Out) principle.

Author: Educational Python Project  
Date: July 28, 2025
"""


class Queue:
    """
    A Queue implementation using Python list as the underlying data structure.
    
    The Queue class provides standard queue operations:
    - enqueue: Add an element to the rear
    - dequeue: Remove and return the front element
    - front: View the front element without removing it
    - is_empty: Check if queue is empty
    - size: Get the number of elements
    
    Attributes:
        _items (list): Internal list to store queue elements
    """
    
    def __init__(self):
        """
        Initialize an empty queue.
        
        The constructor creates an empty list to store queue elements.
        Using a private attribute (_items) to encapsulate the internal structure.
        Front of queue is at index 0, rear is at the end of the list.
        """
        # Initialize empty list to store queue elements
        self._items = []
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        
        This operation has O(1) time complexity as we append to the end of the list.
        
        Args:
            item: The element to be added to the queue (can be any data type)
        
        Returns:
            None
        """
        # Append the item to the end of the list (rear of queue)
        self._items.append(item)
        print(f"Enqueued '{item}' to the queue")
    
    def dequeue(self):
        """
        Remove and return the front element from the queue.
        
        This operation has O(n) time complexity due to list shifting,
        but provides clear FIFO semantics for educational purposes.
        
        Returns:
            The front element from the queue
            
        Raises:
            IndexError: If the queue is empty (underflow condition)
        """
        # Check if queue is empty before dequeuing
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue (Queue Underflow)")
        
        # Remove and return the first element (front of queue)
        dequeued_item = self._items.pop(0)
        print(f"Dequeued '{dequeued_item}' from the queue")
        return dequeued_item
    
    def front(self):
        """
        Return the front element without removing it from the queue.
        
        This operation allows inspection of the front element without modification.
        
        Returns:
            The front element from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        # Check if queue is empty before accessing front
        if self.is_empty():
            raise IndexError("Cannot access front of an empty queue")
        
        # Return the first element without removing it
        front_item = self._items[0]
        print(f"Front element is '{front_item}'")
        return front_item
    
    def rear(self):
        """
        Return the rear element without removing it from the queue.
        
        This operation allows inspection of the rear element without modification.
        
        Returns:
            The rear element from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        # Check if queue is empty before accessing rear
        if self.is_empty():
            raise IndexError("Cannot access rear of an empty queue")
        
        # Return the last element without removing it
        rear_item = self._items[-1]
        print(f"Rear element is '{rear_item}'")
        return rear_item
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        This method provides a clean way to test for empty queue condition.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        # Return True if list length is 0, False otherwise
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of elements in the queue.
        
        This method returns the current size of the queue.
        
        Returns:
            int: Number of elements in the queue
        """
        # Return the length of the internal list
        queue_size = len(self._items)
        print(f"Queue size: {queue_size}")
        return queue_size
    
    def display(self):
        """
        Display the current contents of the queue.
        
        This method provides a visual representation of the queue state.
        Shows elements from front to rear for better understanding.
        
        Returns:
            None
        """
        if self.is_empty():
            print("Queue is empty: []")
        else:
            # Display queue with front and rear elements indicated
            print(f"Queue contents (front to rear): {self._items}")
            print(f"Front -> {self._items[0]}, Rear -> {self._items[-1]}")
    
    def clear(self):
        """
        Remove all elements from the queue.
        
        This method resets the queue to its initial empty state.
        
        Returns:
            None
        """
        # Clear all elements from the internal list
        self._items.clear()
        print("Queue has been cleared")


# Example usage and testing (only runs when script is executed directly)
if __name__ == "__main__":
    print("=== Queue Data Structure Demo ===")
    
    # Create a new queue instance
    queue = Queue()
    
    # Test empty queue
    print("\n1. Testing empty queue:")
    queue.display()
    print(f"Is empty: {queue.is_empty()}")
    
    # Test enqueue operations
    print("\n2. Testing enqueue operations:")
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.display()
    
    # Test front and rear operations
    print("\n3. Testing front and rear operations:")
    queue.front()
    queue.rear()
    queue.display()  # Queue should remain unchanged
    
    # Test dequeue operations
    print("\n4. Testing dequeue operations:")
    queue.dequeue()
    queue.display()
    
    # Test size operation
    print("\n5. Testing size operation:")
    queue.size()
    
    print("\n=== Queue Demo Complete ===")
