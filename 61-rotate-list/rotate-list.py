# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def findNnode(temp: ListNode | None, n:int)->ListNode | None:
    count = 1
    while temp:
        if count == n:
            return temp
        count+=1
        temp = temp.next
    return temp 

    
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head
        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next
        
        if k % length == 0:
            return head
        else:
            k = k%length
        
        tail.next = head
        
        newTail = findNnode(head, length - k)

        newHead = newTail.next
        newTail.next = None

        return newHead
        