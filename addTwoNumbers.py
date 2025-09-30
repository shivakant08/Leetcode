l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

 class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode])->Optional[ListNode]:
        head = ListNode(0)
        root = head
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry

            carry = sum // 10
            head.next = ListNode(sum % 10)
            head = head.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
            
            if carry:
                head.next = ListNode(carry)
                
        return root.next

