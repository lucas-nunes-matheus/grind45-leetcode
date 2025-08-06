class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_begin(self, value):
        new_node = _Node(value)      # Create a new node
        new_node.next = self.head   # Link the new node (next) to the head
        self.head = new_node        # Move the head to the new node 

    def remove_from_begin(self):
        if self.head is None:       # Before to check if next is None, we have to check if head is None
            return None
        removed_value = self.head.value    # Pick the value of head  
        self.head = self.head.next      # Move the head to the next node
        
        return removed_value

    def find_node(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node         # Here, I haven't know what I should return, then, I returned an idx
            current_node = current_node.next
        return None

    def add_to_end(self, value):
        new_node = _Node(value)                 # We create a new node
        if self.head is None:                   # If the LL is empty, we assign the 1st node
            self.head = new_node 

        current_node = self.head                # Otherwise, we'll iterate by this LL
        while current_node.next is not None:    # We iterate until the end of the LL
            current_node = current_node.next
        
        current_node.next = new_node            # At the end, we add the new node

    def add_to_position(self, value, index):

