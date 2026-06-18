class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two halves
        second = slow.next
        slow.next = None

        # 3. Reverse second half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # 4. Merge alternately
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2