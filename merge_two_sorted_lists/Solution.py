# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node for our result list
        resultList = ListNode()

        # Like a pointer to the last node on the list, which we can use to add more elemets to the list.
        resultListCurrent = resultList

        # Handle cases of one or both lists being empty
        if list1 is None and list2 is None:
            return None

        if list1 is None and list2 is not None:
            return list2
        
        if list2 is None and list1 is not None:
            return list1

        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                resultListCurrent.next = list1
                list1 = list1.next
            else:
                resultListCurrent.next = list2
                list2 = list2.next
            
            resultListCurrent = resultListCurrent.next

        # One of the two list pointers will be None. 
        # Add the remaining elements of the non-empty list to the result list
        if list1 is not None:
            while list1 is not None:
                resultListCurrent.next = list1
                list1 = list1.next
                resultListCurrent = resultListCurrent.next
        elif list2 is not None:
            while list2 is not None:
                resultListCurrent.next = list2
                list2 = list2.next
                resultListCurrent = resultListCurrent.next
        
        # Return result list without dummy node
        return resultList.next