class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Inserts a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints the linked list in a visual format."""
        current = self.head
        while current:
            print(f"[ {current.data} ] → ", end="")
            current = current.next
        print("None")
#U - the problem wants us to find the middle node of a singly linked list
#M - very similar two pointer: fast slow
#P - initialize two fast and slow. while the fast is not and fast.next is not None. loop through iterate throught
#the list fast = fast.next.next slow = slow.next. return is slow
    def get_middle_node(self):
        fast = slow = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.data

# Create a linked list and insert some elements
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)

# Print the linked list
print(linked_list.get_middle_node())

