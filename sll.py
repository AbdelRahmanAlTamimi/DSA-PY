class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


class singleLinkList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def traverse_linked_list(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next
        print()

    def search_linked_list(self, target):
        current = self.head
        while current is not None:
            if current.val == target:
                return True
            current = current.next
        return False

    def find_length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_first_node(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp = None

    def remove_last_node(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next
        second_last.next = None

    def delete_at_position(self, position):
        if self.head is None or position < 1:
            return self.head
        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
            return self.head
        current = self.head
        for i in range(1, position - 1):
            if current is not None:
                current = current.next
        if current is None or current.next is None:
            return None
        temp = current.next
        current.next = current.next.next
        temp = None


# Example usage:
sll = singleLinkList()

# Inserting at the beginning
sll.insert_at_beginning("third")
sll.insert_at_beginning("second")
sll.insert_at_beginning("first")
print(sll)  # Output: first -> second -> third

# Inserting after a specific node
sll.insert_after(sll.head.next, "new")
print(sll)  # Output: first -> second -> new -> third

# Inserting at the end
sll.insert_at_end("last")
print(sll)  # Output: first -> second -> new -> third -> last

# Removing the first node
sll.remove_first_node()
print(sll)  # Output: second -> new -> third -> last

# Removing the last node
sll.remove_last_node()
print(sll)  # Output: second -> new -> third

# Deleting a node at a specific position
sll.delete_at_position(2)
print(sll)  # Output: second -> third

# Searching for a value
print(sll.search_linked_list("third"))  # Output: True
print(sll.search_linked_list("fourth"))  # Output: False

# Finding the length of the list
print(sll.find_length())  # Output: 2

# Traversing the list
sll.traverse_linked_list()
# Output:
# second
# third
