from linked_list.ListNode import ListNode

class LinkedList:
    def __init__(self, list):
        self.root = ListNode(list[0])
        ptr = self.root
        for i in range(1, len(list)):
            n = ListNode(list[i])
            ptr.next = n
            ptr = n

    def print_list(self, head):
        print()
        n = head
        while n:
            print(str(n.val) + ' ->', end=' ')
            n = n.next
        print()

if __name__ == '__main__':
    linked_list = LinkedList([1, 2, 3, 4, 5])
    linked_list.print_list(linked_list.root)