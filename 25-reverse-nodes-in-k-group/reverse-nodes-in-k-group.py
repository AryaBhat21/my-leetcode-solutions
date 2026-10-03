# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_knode(temp:ListNode | None,k:int)->ListNode | None:
    k = k-1
    while temp and k>0:
        k=k-1
        temp=temp.next
    return temp

def reverse_ll(head:ListNode | None)->ListNode | None:
    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front
    return prev

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        prevLast = None
        temp = head
        while temp:
            k_node = get_knode(temp,k)
            if k_node is None:
                if prevLast is not None:
                    prevLast.next = temp
                break
            nextNode = k_node.next
            k_node.next = None
            reverse_ll(temp)
            if temp==head:
                head = k_node
            else:
                prevLast.next = k_node
            prevLast = temp
            temp = nextNode
        return head

        