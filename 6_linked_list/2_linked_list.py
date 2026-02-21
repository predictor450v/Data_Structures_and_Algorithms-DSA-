# linked list implementation in Python
class Node:  # class to represent a node in the linked list
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # constructor to initialize the head of the linked list
    def __init__(self):
        self.head = None

        # 
# insert at beginning of linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):  # print the linked list
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'   # concatenate the data of each node to the string with an arrow
            itr = itr.next
        print(llstr)  # print the final string representation of the linked list

    # insert at end of linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:  # traverse to the end of the linked list
            itr = itr.next
        itr.next = Node(data, None)  # create a new node and set it as the next of the last node

    # insert values from a list to the linked list
    def insert_values(self, data_list):
        self.head = None  # reset the linked list
        for data in data_list:  # insert each value from the list to the linked list
            self.insert_at_end(data)
    
    # get length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    

if __name__ == '__main__':   # test the linked list implementation
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(23)
    ll.insert_at_beginning(90)
    ll.print()

    ll.insert_at_end(100)
    ll.print()

    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print()

    print('Length of linked list:', ll.get_length())
