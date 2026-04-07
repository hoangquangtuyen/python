class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next= next
    
class Solution:
    def deleteDuplicates(self, head):
        current= head
        while current and current.next:
            if current.val == current.next.val:
                current.next= current.next.next
        
            else:
                current= current.next
        return head

def build_list(values):
    head = ListNode(values[0])
    current= head
    for i in values[1:]:
        current.next= ListNode(i)
        current= current.next
    return head

def print_list(head):
    while head:
        print(head.val, end= '')
        head= head.next


values= [1,1,2,3,3]
head= build_list(values)
s= Solution()
new_head= s.deleteDuplicates(head)
print_list(new_head)