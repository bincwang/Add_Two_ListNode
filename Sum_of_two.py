# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def add_data(self, root, x):      
        curr = root
        if curr.val==None:
            curr.val = x
            root = curr
            return root
        while curr.next != None:
            curr = curr.next
        
        curr.next = ListNode(x)
        
        return root
                
            
    def numerize(self,x):
        value = 0
        i = 1
        while x != None:
            value = value + (x.val * i)
            x = x.next
            i = i * 10
        return value
              
    def reverse(self,x):
        c = str(x)
        root = ListNode(None)
        for i in reversed(c):
            num = int(i)
            root = self.add_data(root, num)
        return root
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = self.numerize(l1) + self.numerize(l2)
        result = ListNode(None)
        result = self.reverse(total)
        return result
