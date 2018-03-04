# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:           
    #transfer the singly-linked list to number        
    def numerize(self,x):
        value = 0
        i = 1
        while x != None:
            value = value + (x.val * i)
            x = x.next
            i = i * 10
        return value
    #transfer number to a singly-linked list          
    def reverse(self,x):
        root = ListNode(int(str(x)[-1]))
        curr = root
        for i in reversed(str(x)[:len(str(x))-1]):
            num = int(i)
            curr.next = ListNode(num)
            curr = curr.next
        return root
    #our OG function, which connects two linked list and calculate the new output of the linked list
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = self.numerize(l1) + self.numerize(l2)
        result = self.reverse(total)
        return result
        
def main():
    return 
if __name__ == "__main__":
    main()
        
