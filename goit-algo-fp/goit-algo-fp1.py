"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class Node:
    def __init__(self, data: int=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node()
        tail = dummy
        a, b = self.head, other.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            if sorted_list.head is None or sorted_list.head.data >= current.data:
                current.next = sorted_list.head
                sorted_list.head = current
            else:
                sorted_current = sorted_list.head
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list.head

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_beginning(6)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(98)
    llist.insert_at_beginning(100)
    llist.insert_at_beginning(101)
    llist.insert_at_beginning(18)

    print("Original list:")
    llist.print_list()

    print("\nReversed list:")
    llist.reverse_list()
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_end(1)
    llist2.insert_at_end(3)
    llist2.insert_at_end(7)
    llist2.insert_at_end(9)

    print("\nMerged list:")
    llist.sorted_merge(llist2)
    llist.print_list()

    print("\nSorted list:")
    llist.insertion_sort()
    llist.print_list()