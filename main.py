"""
Main Application Demonstrating Stack, Queue, and Linked List Integration

This application demonstrates the practical usage and interaction of all three
data structures (Stack, Queue, and Linked List) in a cohesive system.
It showcases how these fundamental data structures can work together to solve
real-world problems while applying software construction principles.

Author: Educational Python Project
Date: July 28, 2025
"""

# Import all three data structure modules
# This demonstrates modular design and low coupling
from stack import Stack
from queue import Queue
from linkedlist import LinkedList


class DataStructureManager:
    """
    A manager class that coordinates the use of Stack, Queue, and Linked List.
    
    This class demonstrates how multiple data structures can work together
    in a larger system while maintaining high cohesion and clear responsibilities.
    
    Attributes:
        stack (Stack): Stack instance for LIFO operations
        queue (Queue): Queue instance for FIFO operations  
        linked_list (LinkedList): Linked List instance for flexible data storage
    """
    
    def __init__(self):
        """
        Initialize the data structure manager with instances of all three structures.
        
        This constructor demonstrates dependency injection and composition patterns.
        """
        # Create instances of all three data structures
        self.stack = Stack()
        self.queue = Queue() 
        self.linked_list = LinkedList()
        
        print("=== Data Structure Manager Initialized ===")
        print("Stack, Queue, and Linked List are ready for use!")
    
    def demonstrate_basic_operations(self):
        """
        Demonstrate basic operations for each data structure.
        
        This method shows the fundamental operations of each structure
        with clear examples and educational commentary.
        """
        print("\n" + "="*60)
        print("BASIC OPERATIONS DEMONSTRATION")
        print("="*60)
        
        # Stack Operations Demo
        print("\n--- STACK OPERATIONS (LIFO - Last In, First Out) ---")
        print("Adding elements to stack (push operations):")
        self.stack.push("Task 1")
        self.stack.push("Task 2") 
        self.stack.push("Task 3")
        
        print("\nStack contents:")
        self.stack.display()
        
        print("\nRemoving elements from stack (pop operations):")
        self.stack.pop()
        self.stack.display()
        
        print("\nPeeking at top element:")
        self.stack.peek()
        
        # Queue Operations Demo
        print("\n--- QUEUE OPERATIONS (FIFO - First In, First Out) ---")
        print("Adding customers to queue (enqueue operations):")
        self.queue.enqueue("Customer A")
        self.queue.enqueue("Customer B")
        self.queue.enqueue("Customer C")
        
        print("\nQueue contents:")
        self.queue.display()
        
        print("\nServing customers from queue (dequeue operations):")
        self.queue.dequeue()
        self.queue.display()
        
        print("\nChecking front and rear of queue:")
        self.queue.front()
        self.queue.rear()
        
        # Linked List Operations Demo
        print("\n--- LINKED LIST OPERATIONS (Dynamic Data Storage) ---")
        print("Building a linked list with various insertion methods:")
        self.linked_list.insert_at_beginning("Header")
        self.linked_list.insert_at_end("Footer") 
        self.linked_list.insert_at_position("Content 1", 1)
        self.linked_list.insert_at_position("Content 2", 2)
        
        print("\nLinked list contents:")
        self.linked_list.display()
        
        print("\nSearching in linked list:")
        self.linked_list.search("Content 1")
        
        print("\nAccessing element by position:")
        self.linked_list.get_at_position(1)
    
    def demonstrate_integration_scenario(self):
        """
        Demonstrate how the three data structures can work together 
        in a practical scenario: A Task Processing System.
        
        This scenario shows:
        - Queue for incoming tasks (FIFO processing)
        - Stack for undo operations (LIFO for reversals)
        - Linked List for maintaining task history
        """
        print("\n" + "="*60)
        print("INTEGRATION SCENARIO: TASK PROCESSING SYSTEM")
        print("="*60)
        
        # Clear all structures for fresh demonstration
        self.stack.clear()
        self.queue.clear()
        self.linked_list.clear()
        
        print("\nScenario: A task management system that processes tasks,")
        print("maintains history, and supports undo operations.")
        
        # Step 1: Add tasks to processing queue
        print("\n1. ADDING TASKS TO PROCESSING QUEUE")
        print("   Tasks arrive and are queued for processing (FIFO):")
        tasks = ["Email Report", "Update Database", "Backup Files", "Send Notifications"]
        
        for task in tasks:
            self.queue.enqueue(task)
        
        print(f"\n   Current queue status:")
        self.queue.display()
        
        # Step 2: Process tasks and maintain history
        print("\n2. PROCESSING TASKS AND MAINTAINING HISTORY")
        print("   As tasks are processed, they're added to history and undo stack:")
        
        completed_tasks = []
        
        # Process half the tasks
        for i in range(2):
            # Get next task from queue
            if not self.queue.is_empty():
                current_task = self.queue.dequeue()
                
                # Add to completed tasks list
                completed_tasks.append(current_task)
                
                # Add to undo stack (in case we need to reverse)
                self.stack.push(current_task)
                
                # Add to history linked list
                self.linked_list.insert_at_end(current_task)
                
                print(f"   Processed: {current_task}")
        
        print(f"\n   Remaining tasks in queue:")
        self.queue.display()
        
        print(f"\n   Task history (linked list):")
        self.linked_list.display()
        
        print(f"\n   Undo stack (most recent first):")
        self.stack.display()
        
        # Step 3: Demonstrate undo operation
        print("\n3. UNDO OPERATION")
        print("   Something went wrong! Let's undo the last task:")
        
        if not self.stack.is_empty():
            # Get the last completed task from undo stack
            last_task = self.stack.pop()
            
            # Remove from completed tasks
            completed_tasks.remove(last_task)
            
            # Add back to front of processing queue (high priority)
            # Note: We'll create a new queue with this task first
            temp_queue = Queue()
            temp_queue.enqueue(last_task)
            
            # Add remaining queue items
            while not self.queue.is_empty():
                temp_queue.enqueue(self.queue.dequeue())
            
            # Replace the queue
            self.queue = temp_queue
            
            print(f"   Undid task: {last_task}")
            print(f"   Task returned to front of queue for reprocessing")
        
        print(f"\n   Updated queue after undo:")
        self.queue.display()
        
        print(f"\n   Updated undo stack:")
        self.stack.display()
        
        # Step 4: Search and retrieve from history
        print("\n4. SEARCHING TASK HISTORY")
        print("   Looking up previously completed tasks:")
        
        search_task = "Email Report"
        position = self.linked_list.search(search_task)
        
        if position != -1:
            print(f"   Found '{search_task}' in history at position {position}")
        
        # Step 5: Show final state
        print("\n5. FINAL SYSTEM STATE")
        print(f"   Tasks pending in queue: {self.queue.size()}")
        print(f"   Tasks available for undo: {self.stack.size()}")
        print(f"   Tasks in history: {self.linked_list.size()}")
    
    def demonstrate_data_flow(self):
        """
        Demonstrate how data flows between the three structures.
        
        This shows practical data transfer and transformation scenarios.
        """
        print("\n" + "="*60)
        print("DATA FLOW DEMONSTRATION")
        print("="*60)
        
        # Clear all structures
        self.stack.clear()
        self.queue.clear()
        self.linked_list.clear()
        
        print("\nDemonstrating data transfer between structures:")
        
        # Step 1: Populate linked list with data
        print("\n1. Populating linked list with initial data:")
        data_items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
        
        for item in data_items:
            self.linked_list.insert_at_end(item)
        
        self.linked_list.display()
        
        # Step 2: Transfer data from linked list to queue
        print("\n2. Transferring data from linked list to queue:")
        print("   (Reading linked list sequentially)")
        
        # Read all items from linked list and add to queue
        for i in range(self.linked_list.size()):
            item = self.linked_list.get_at_position(i)
            self.queue.enqueue(item)
        
        print("\n   Queue after transfer:")
        self.queue.display()
        
        # Step 3: Process queue items and push results to stack
        print("\n3. Processing queue items and stacking results:")
        print("   (Processing with FIFO order, stacking with LIFO order)")
        
        processed_count = 0
        while not self.queue.is_empty() and processed_count < 3:
            # Dequeue item from front
            item = self.queue.dequeue()
            
            # Process the item (simulate processing by adding "Processed: " prefix)
            processed_item = f"Processed: {item}"
            
            # Push result to stack
            self.stack.push(processed_item)
            
            processed_count += 1
        
        print("\n   Stack after processing:")
        self.stack.display()
        
        print("\n   Remaining items in queue:")
        self.queue.display()
        
        # Step 4: Demonstrate reverse processing using stack
        print("\n4. Reverse processing using stack (LIFO order):")
        
        while not self.stack.is_empty():
            processed_item = self.stack.pop()
            print(f"   Retrieved from stack: {processed_item}")
    
    def demonstrate_error_handling(self):
        """
        Demonstrate error handling and edge cases for all data structures.
        
        This shows proper exception handling and defensive programming.
        """
        print("\n" + "="*60)
        print("ERROR HANDLING DEMONSTRATION")  
        print("="*60)
        
        # Clear all structures
        self.stack.clear()
        self.queue.clear()
        self.linked_list.clear()
        
        print("\nDemonstrating error handling and edge cases:")
        
        # Stack error handling
        print("\n1. STACK ERROR HANDLING:")
        
        try:
            print("   Attempting to pop from empty stack:")
            self.stack.pop()
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        try:
            print("   Attempting to peek at empty stack:")
            self.stack.peek()
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        # Queue error handling
        print("\n2. QUEUE ERROR HANDLING:")
        
        try:
            print("   Attempting to dequeue from empty queue:")
            self.queue.dequeue()
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        try:
            print("   Attempting to access front of empty queue:")
            self.queue.front()
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        # Linked List error handling
        print("\n3. LINKED LIST ERROR HANDLING:")
        
        try:
            print("   Attempting to access invalid position in empty list:")
            self.linked_list.get_at_position(0)
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        try:
            print("   Attempting to delete from empty list:")
            self.linked_list.delete_at_position(0)
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        # Add some data and test boundary conditions
        print("\n4. BOUNDARY CONDITION TESTING:")
        
        self.linked_list.insert_at_end("Test Item")
        
        try:
            print("   Attempting to access position beyond list size:")
            self.linked_list.get_at_position(5)
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
        
        try:
            print("   Attempting to insert at invalid position:")
            self.linked_list.insert_at_position("Invalid", -1)
        except IndexError as e:
            print(f"   ✓ Caught expected error: {e}")
    
    def display_summary(self):
        """
        Display a summary of all data structures and their current states.
        
        This provides a comprehensive overview of the system state.
        """
        print("\n" + "="*60)
        print("SYSTEM SUMMARY")
        print("="*60)
        
        print("\nCurrent state of all data structures:")
        
        print("\n--- Stack Status ---")
        if self.stack.is_empty():
            print("Stack is empty")
        else:
            self.stack.display()
            self.stack.size()
        
        print("\n--- Queue Status ---")
        if self.queue.is_empty():
            print("Queue is empty")
        else:
            self.queue.display()
            self.queue.size()
        
        print("\n--- Linked List Status ---")
        if self.linked_list.is_empty():
            print("Linked List is empty")
        else:
            self.linked_list.display()
            self.linked_list.size()


def main():
    """
    Main function that orchestrates the entire demonstration.
    
    This function shows the proper way to structure a main program
    that uses multiple data structures in a coordinated fashion.
    """
    print("="*80)
    print("EDUCATIONAL DATA STRUCTURES PROJECT")
    print("Stack, Queue, and Linked List Integration Demo")
    print("="*80)
    
    # Create the data structure manager
    # This demonstrates composition and dependency management
    manager = DataStructureManager()
    
    try:
        # Run all demonstrations
        manager.demonstrate_basic_operations()
        manager.demonstrate_integration_scenario()
        manager.demonstrate_data_flow()
        manager.demonstrate_error_handling()
        manager.display_summary()
        
        print("\n" + "="*80)
        print("SOFTWARE CONSTRUCTION PRINCIPLES DEMONSTRATED:")
        print("="*80)
        print("✓ MODULAR DESIGN: Separate modules for each data structure")
        print("✓ HIGH COHESION: Each class has a single, well-defined responsibility")
        print("✓ LOW COUPLING: Minimal dependencies between modules")
        print("✓ CLEAR NAMING: Descriptive names for all variables and functions")
        print("✓ DOCUMENTATION: Comprehensive comments and docstrings")
        print("✓ ERROR HANDLING: Proper exception handling for edge cases")
        print("✓ ENCAPSULATION: Private attributes and public interfaces")
        print("✓ REUSABILITY: Components can be used independently")
        
        print("\n" + "="*80)
        print("EDUCATIONAL OBJECTIVES ACHIEVED:")
        print("="*80)
        print("✓ Stack implementation with LIFO behavior")
        print("✓ Queue implementation with FIFO behavior")
        print("✓ Linked List implementation with dynamic memory allocation")
        print("✓ Integration of multiple data structures")
        print("✓ Real-world application scenarios")
        print("✓ Error handling and edge case management")
        print("✓ Software engineering best practices")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("This demonstrates the importance of proper error handling!")
    
    finally:
        print("\n" + "="*80)
        print("DEMONSTRATION COMPLETE")
        print("Thank you for exploring data structures!")
        print("="*80)


# Entry point - only run when this script is executed directly
if __name__ == "__main__":
    main()
