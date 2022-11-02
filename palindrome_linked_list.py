# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middle(head)  #passing the head to the middle function to find the middle of the linked list
        midNext = mid.next  #cutting the linkedlist into two
        mid.next = None
        rev = self.reversefunc(midNext)  #passing the second half of the linked list to the reverse function
        
        while rev:  #checking whether the two linked list are palindrome or not
            if head.val == rev.val: #if the head of the first list and head of the second list if true we are changing the pointer to the next val
                head = head.next
                rev = rev.next
            else:  #if it is not palindrome we are returning false, if it is palindrome we are returning true after the loop is done completely
                return False
        return True
        
    def middle(self,head):  #middle function
        slow = head #placing the slow and fast pointer at the head
        fast = head
        while fast.next!=None and fast.next.next!=None:  #until both the pointers are null we are moving the slow pointer by 1 and fast pointer by 2
            slow = slow.next
            fast = fast.next.next

        return slow  #we are returning the middle val 
        
    
        
    def reversefunc(self,head): #reverse function
        curr = head  #curr is head and prev is none
        prev = None

        while curr!=None: #till curr is equal to none the loop will run
            temp = curr.next  #storing the curr.next in temp
            curr.next = prev #we are cahning the curr node pointer to prev
            prev = curr #prev is curr
            curr= temp  #curr is temp
        return prev #we are returning the prev
            
        
        
            
        
        
            
        
            
            
            
        
            
            
        