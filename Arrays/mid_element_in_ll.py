class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_value(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print("{} ".format(temp.data),end='')
                temp = temp.next
    def mid_ele_in_ll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        one = self.head
        two = self
        while temp:
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_value(10)
    ll.insert_value(20)
    ll.insert_value(30)
    ll.insert_value(40)
    ll.insert_value(50)
    ll.print_list()